"""
dfa_security: simple deterministic-rule engine that inspects endpoint specs
and returns a secured transformation of the spec, plus an audit of applied rules.

Design notes:
- We represent rules as Python functions that check the endpoint and return a transformation + note.
- Rules are applied deterministically in a fixed order (so it behaves like a DFA transition chain).
- Easy to extend: add new rule functions to RULES list.
"""

from typing import Dict, Any, Tuple, List
import jwt
import os
from passlib.hash import bcrypt

SECRET = os.environ.get('TOC_SECRET', 'supersecretkey')

def rule_login_to_jwt(spec: Dict[str, Any]) -> Tuple[Dict[str, Any], List[str]]:
    """
    If endpoint name or path contains 'login' and body has 'username' and 'password',
    transform to expect single 'auth_token' in the request. Keep a note that server is
    expected to accept a JWT and validate it.
    """
    notes = []
    spec2 = dict(spec)  # shallow copy
    name = spec.get('name','').lower()
    path = spec.get('path','').lower()
    body = spec.get('body_schema',{})

    if ('login' in name or 'login' in path) and ('username' in body and 'password' in body):
        # produce secured body schema
        secured_body = {
            "auth_token": {"type":"string", "format":"jwt", "description":"JWT carrying credentials or proof"}
        }
        spec2['body_schema'] = secured_body
        # include server-side expectation notes
        spec2.setdefault('security_meta',{})
        spec2['security_meta']['login_mode'] = 'jwt'
        notes.append("Transformed login username/password -> auth_token (JWT).")
    return spec2, notes

def rule_hash_password_storage(spec: Dict[str, Any]) -> Tuple[Dict[str, Any], List[str]]:
    """
    If endpoint body or response mentions 'password' field in response or storage hints,
    mark it to be stored as hashed_password (bcrypt) and add note.
    """
    notes = []
    spec2 = dict(spec)
    # check body_schema and response_schema for password fields
    for k in ('body_schema','response_schema'):
        schema = spec.get(k, {})
        if not isinstance(schema, dict):
            continue
        if 'password' in schema:
            schema2 = dict(schema)
            schema2.pop('password', None)
            schema2['hashed_password'] = {"type":"string", "description":"bcrypt hash of password"}
            spec2[k] = schema2
            notes.append(f"Replaced `{k}.password` with `hashed_password` to avoid storing plain passwords.")
    return spec2, notes

def rule_require_https(spec: Dict[str, Any]) -> Tuple[Dict[str, Any], List[str]]:
    notes = []
    spec2 = dict(spec)
    # For any endpoint that looks sensitive (login, register, password reset), enforce https flag
    name = spec.get('name','').lower()
    path = spec.get('path','').lower()
    if any(x in name or x in path for x in ['login','register','password','reset','change-password']):
        spec2.setdefault('security_meta', {})
        spec2['security_meta']['require_https'] = True
        notes.append("Marked endpoint as require_https=True (sensitive).")
    return spec2, notes

def rule_rate_limit_header(spec: Dict[str, Any]) -> Tuple[Dict[str, Any], List[str]]:
    """
    Add a rate-limit recommendation for endpoints likely to be abused: login, password reset.
    """
    notes = []
    spec2 = dict(spec)
    name = spec.get('name','').lower()
    path = spec.get('path','').lower()
    if any(x in name or x in path for x in ['login','reset','auth']):
        spec2.setdefault('security_meta', {})
        spec2['security_meta']['rate_limit'] = {'requests_per_min': 30}
        notes.append("Applied default rate-limit (30 req/min) for auth-related endpoint.")
    return spec2, notes

# Put rules in deterministic order (this is our "DFA" transition order)
RULES = [
    rule_login_to_jwt,
    rule_hash_password_storage,
    rule_require_https,
    rule_rate_limit_header
]

def apply_security_dfa(endpoint_spec: Dict[str, Any]) -> Dict[str, Any]:
    """
    Apply each rule in RULES in order; accumulate notes and return transformed spec with 'applied_rules'.
    endpoint_spec expected to be a dict:
      { name, path, method, query_schema(dict), body_schema(dict), response_schema(dict) }
    """
    spec = dict(endpoint_spec)
    applied = []
    for rule in RULES:
        new_spec, notes = rule(spec)
        if notes:
            applied.extend(notes)
        spec = new_spec
    spec['applied_rules'] = applied
    return spec

# helper: create JWT for 'login' demonstration (server side)
def create_login_jwt(claims: dict, expires_in: int = 300) -> str:
    payload = dict(claims)
    # minimal expiry handling - real app should set exp
    token = jwt.encode(payload, SECRET, algorithm='HS256')
    return token

# helper: verify jwt
def verify_login_jwt(token: str) -> dict:
    try:
        data = jwt.decode(token, SECRET, algorithms=['HS256'])
        return data
    except Exception as e:
        raise
