
import itertools, json
from automata.regex_nfa import epsilon_closure, move
import numpy as np

def nfa_to_dfa(nfa):
    # DFA: states are frozenset of NFA states
    start = frozenset(epsilon_closure(nfa, {nfa.start}))
    unmarked = [start]
    dtrans = {}
    accepts = set()
    alphabet = set()
    for a,m in nfa.trans.items():
        for sym in m.keys():
            if sym != '': alphabet.add(sym)
    while unmarked:
        T = unmarked.pop()
        if T not in dtrans:
            dtrans[T] = {}
        for a in alphabet:
            U = frozenset(epsilon_closure(nfa, move(nfa, T, a)))
            if not U:
                continue
            dtrans[T][a] = U
            if U not in dtrans:
                unmarked.append(U)
    for S in list(dtrans.keys()):
        for s in S:
            if s in nfa.accepts:
                accepts.add(S)
                break
    dfa = {'start': start, 'states': set(dtrans.keys()), 'accepts': accepts, 'trans': dtrans}
    return dfa

def simulate_dfa(dfa, s):
    cur = dfa['start']
    for ch in s:
        if ch in dfa['trans'].get(cur, {}):
            cur = dfa['trans'][cur][ch]
        else:
            return False
    return cur in dfa['accepts']

def dfa_to_dot(dfa):
    lines = []
    lines.append(f"start: {sorted(list(dfa['start']))}")
    lines.append("accepts: " + ",".join(sorted(['|'.join(sorted(x)) for x in dfa['accepts']]))) 
    for a,m in dfa['trans'].items():
        for sym,d in m.items():
            lines.append(f"{sorted(list(a))} -[{sym}]-> {sorted(list(d))}")
    return "\\n".join(lines)

def minimize_dfa(dfa):
    # Hopcroft-like partition refinement (simple implementation)
    states = list(dfa['states'])
    accepts = set(dfa['accepts'])
    non_accepts = set(states) - accepts
    P = [accepts, non_accepts]
    W = [accepts.copy() if isinstance(accepts, set) else set(accepts)]
    alphabet = set()
    for a,m in dfa['trans'].items():
        for sym in m.keys():
            alphabet.add(sym)
    while W:
        A = W.pop()
        for c in list(alphabet):
            X = set()
            for s in states:
                dest = dfa['trans'].get(s, {}).get(c, None)
                if dest and dest in A:
                    X.add(s)
            newP = []
            for Y in P:
                intersect = Y & X
                diff = Y - X
                if intersect and diff:
                    newP.append(intersect)
                    newP.append(diff)
                    if Y in W:
                        W.remove(Y)
                        W.append(intersect); W.append(diff)
                    else:
                        if len(intersect) <= len(diff):
                            W.append(intersect)
                        else:
                            W.append(diff)
                else:
                    newP.append(Y)
            P = newP
    # build new DFA
    rep = {frozenset(part): 'S'+str(i) for i,part in enumerate(P)}
    new_trans = {}
    new_accepts = set()
    new_start = None
    for part in P:
        name = rep[frozenset(part)]
        anystate = next(iter(part)) if part else None
        if anystate in dfa['accepts']:
            new_accepts.add(name)
        if dfa['start'] in part:
            new_start = name
        new_trans[name] = {}
        for sym in alphabet:
            dest = dfa['trans'].get(anystate, {}).get(sym, None) if anystate else None
            dest_name = None
            if dest:
                for part2 in P:
                    if dest in part2:
                        dest_name = rep[frozenset(part2)]; break
            if dest_name:
                new_trans[name][sym] = dest_name
    new_states = set(new_trans.keys())
    new_dfa = {'start': new_start, 'states': new_states, 'accepts': new_accepts, 'trans': new_trans}
    return new_dfa
