"""
Richer DFA engine with explicit Rule objects and DFA builder.

Design:
- Each Rule has an id, description, trigger (checks 'symbols'), transform (applies to spec),
  and explanation string.
- RULES is an ordered list. We create an explicit DFA where each stage S_i corresponds
  to "after evaluating rule i" (S0 = start). Transitions record whether the rule applied.
- simulate_dfa_on_spec returns the DFA and also 'applied_rules' and 'steps' to easily step-through.
"""

from typing import Dict, Any, Callable
import os, copy, jwt

SECRET = os.environ.get('TOC_SECRET', 'dev_secret')

def extract_symbols(endpoint: Dict[str, Any]) -> Dict[str, bool]:
    name = (endpoint.get('name') or '').lower()
    path = (endpoint.get('path') or '').lower()
    body = endpoint.get('body_schema') or {}
    response = endpoint.get('response_schema') or {}
    s = {}
    s['is_login'] = ('login' in name or 'login' in path)
    s['has_user_pass'] = ('username' in body and 'password' in body)
    s['has_password_field'] = ('password' in body or 'password' in response)
    s['is_sensitive'] = any(k in name or k in path for k in ['login','register','password','reset','auth'])
    s['returns_password'] = ('password' in response)
    return s

class Rule:
    def __init__(self, id: str, description: str,
                 trigger: Callable[[Dict[str, bool]], bool],
                 transform: Callable[[Dict[str, Any]], Dict[str, Any]],
                 explanation: str):
        self.id = id
        self.description = description
        self.trigger = trigger
        self.transform = transform
        self.explanation = explanation

# --- Rule Definitions ---

def trigger_login_to_jwt(symbols):
    return symbols.get('is_login') and symbols.get('has_user_pass')

def transform_login_to_jwt(spec):
    new = copy.deepcopy(spec)
    new['body_schema'] = {
        'auth_token': {'type': 'string', 'format': 'jwt', 'description': 'JWT containing credentials/proof'}
    }
    new.setdefault('security_meta', {})
    new['security_meta']['login_mode'] = 'jwt'
    return new

rule_login_to_jwt = Rule(
    id='login_to_jwt',
    description='Replace username/password with auth_token (JWT)',
    trigger=trigger_login_to_jwt,
    transform=transform_login_to_jwt,
    explanation='Login endpoints carrying raw username/password are transformed to accept a single auth_token (JWT). '
                'This reduces exposure of credentials on the wire and centralizes verification.'
)

def trigger_hash_password(symbols):
    return symbols.get('has_password_field')

def transform_hash_password(spec):
    new = copy.deepcopy(spec)
    for k in ('body_schema', 'response_schema'):
        sch = new.get(k) or {}
        if isinstance(sch, dict) and 'password' in sch:
            sch.pop('password', None)
            sch['hashed_password'] = {'type': 'string', 'description': 'bcrypt hash'}
            new[k] = sch
    return new

rule_hash_password = Rule(
    id='hash_password_storage',
    description='Replace password fields with hashed_password (bcrypt)',
    trigger=trigger_hash_password,
    transform=transform_hash_password,
    explanation='Any schema fields named password are replaced with hashed_password to emphasize that servers should store only hashes.'
)

def trigger_require_https(symbols):
    return symbols.get('is_sensitive')

def transform_require_https(spec):
    new = copy.deepcopy(spec)
    new.setdefault('security_meta', {})
    new['security_meta']['require_https'] = True
    return new

rule_require_https = Rule(
    id='require_https',
    description='Mark endpoint as requiring HTTPS transport',
    trigger=trigger_require_https,
    transform=transform_require_https,
    explanation='Sensitive endpoints must require TLS/HTTPS to protect data in transit.'
)

def trigger_rate_limit(symbols):
    return symbols.get('is_sensitive')

def transform_rate_limit(spec):
    new = copy.deepcopy(spec)
    new.setdefault('security_meta', {})
    new['security_meta']['rate_limit'] = {'requests_per_min': 30}
    return new

rule_rate_limit = Rule(
    id='rate_limit_30pm',
    description='Apply default rate limit for sensitive endpoints',
    trigger=trigger_rate_limit,
    transform=transform_rate_limit,
    explanation='Applying rate limits reduces brute-force and abuse potential on auth endpoints.'
)

RULES = [rule_login_to_jwt, rule_hash_password, rule_require_https, rule_rate_limit]

# --- DFA builder & simulator ---

def build_dfa_from_spec(spec: Dict[str, Any]) -> Dict[str, Any]:
    """
    Build explicit DFA representation of the pipeline.
    states: list of state names S0..SN
    transitions: mapping state -> { 'applies': next, 'not_applies': self or next depending on design }
    state_info: per-state metadata (snapshot, applied_rule, explanation)
    final_spec: the spec after applying all rules that triggered.
    rules_meta: short metadata describing each rule in order.
    """
    states = []
    transitions = {}
    state_info = {}
    current = copy.deepcopy(spec)
    states.append('S0')
    state_info['S0'] = {'desc': 'Start: no rules applied', 'spec': current, 'applied_rule': None}
    transitions['S0'] = {}

    for i, rule in enumerate(RULES):
        sname = f'S{i}'
        tname = f'S{i+1}'
        cur_symbols = extract_symbols(current)
        triggered = rule.trigger(cur_symbols)
        if triggered:
            new_spec = rule.transform(current)
            states.append(tname)
            transitions.setdefault(sname, {})
            transitions[sname]['applies'] = tname
            transitions[sname]['not_applies'] = sname
            state_info[tname] = {
                'desc': f'After applying rule: {rule.description}',
                'spec': new_spec,
                'applied_rule': rule.id,
                'explanation': rule.explanation
            }
            current = new_spec
        else:
            states.append(tname)
            transitions.setdefault(sname, {})
            transitions[sname]['applies'] = tname
            state_info[tname] = {
                'desc': f'Rule evaluated but not applied: {rule.description}',
                'spec': current,
                'applied_rule': None,
                'explanation': rule.explanation
            }

    accept = f'S{len(RULES)}'
    dfa = {
        'states': states,
        'start': 'S0',
        'accepts': [accept],
        'transitions': transitions,
        'state_info': state_info,
        'symbols': extract_symbols(spec),
        'final_spec': current,
        'rules_meta': [{'id': r.id, 'description': r.description, 'explanation': r.explanation} for r in RULES]
    }
    return dfa

def simulate_dfa_on_spec(spec: Dict[str, Any]) -> Dict[str, Any]:
    dfa = build_dfa_from_spec(spec)
    state = dfa['start']
    applied = []
    steps = []
    for i in range(len(RULES)):
        trans = dfa['transitions'].get(state, {})
        next_state = trans.get('applies') or trans.get('not_applies')
        info = dfa['state_info'].get(next_state, {})
        if info.get('applied_rule'):
            applied.append(info['applied_rule'])
        steps.append({'from': state, 'to': next_state, 'info': info})
        state = next_state
    dfa['applied_rules'] = applied
    dfa['steps'] = steps
    return dfa
