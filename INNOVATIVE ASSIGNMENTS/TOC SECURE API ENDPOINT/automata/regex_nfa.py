
# Simple regex -> NFA (supports concatenation, | (union), * (kleene), parentheses)
# Using Thompson's construction.
# NFA represented as dict: { 'states': set, 'start': s, 'accepts': set, 'trans': {state: {symbol: set(states), '': set(epsilon_states)}} }

class NFA:
    def __init__(self):
        self.states = set()
        self.start = None
        self.accepts = set()
        self.trans = {}  # state -> {symbol: set(dest)}

    def add_state(self, s):
        self.states.add(s)
        self.trans.setdefault(s, {})

    def add_edge(self, a, symbol, b):
        self.add_state(a); self.add_state(b)
        self.trans.setdefault(a, {}).setdefault(symbol, set()).add(b)

def new_state(counter=[0]):
    counter[0] += 1
    return 'q' + str(counter[0])

def regex_to_postfix(regex):
    # insert explicit concatenation operator '.' where needed
    output = []
    stack = []
    prec = {'*':3, '.':2, '|':1}
    # add concatenation
    newr = ''
    prev = None
    for c in regex:
        if c == ' ':
            continue
        if prev:
            if (prev not in '(|' and c not in '|)*'):
                newr += '.'
        newr += c
        prev = c
    regex = newr
    for c in regex:
        if c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError('Mismatched parentheses')
            stack.pop()
        elif c in prec:
            while stack and stack[-1] != '(' and prec.get(stack[-1],0) >= prec[c]:
                output.append(stack.pop())
            stack.append(c)
        else:
            output.append(c)
    while stack:
        output.append(stack.pop())
    return ''.join(output)

def postfix_to_nfa(postfix):
    stack = []
    for c in postfix:
        if c == '*':
            n = stack.pop()
            # kleene
            s = new_state(); f = new_state()
            nfa = NFA()
            nfa.add_state(s); nfa.add_state(f)
            # copy states and transitions from n
            offset_map = {}
            for st in n.states:
                ns = new_state()
                offset_map[st] = ns
                nfa.add_state(offset_map[st])
            for a, m in n.trans.items():
                for sym, dests in m.items():
                    for d in dests:
                        nfa.add_edge(offset_map[a], sym, offset_map[d])
            # connect
            nfa.add_edge(s, '', offset_map[n.start])
            for acc in n.accepts:
                nfa.add_edge(offset_map[acc], '', offset_map[n.start])
                nfa.add_edge(offset_map[acc], '', f)
            nfa.add_edge(s, '', f)
            nfa.start = s; nfa.accepts = {f}
            stack.append(nfa)
        elif c == '.':
            n2 = stack.pop(); n1 = stack.pop()
            nfa = NFA()
            map1 = {}; map2 = {}
            for st in n1.states:
                ns = new_state(); map1[st] = ns; nfa.add_state(ns)
            for st in n2.states:
                ns = new_state(); map2[st] = ns; nfa.add_state(ns)
            for a,m in n1.trans.items():
                for sym,dests in m.items():
                    for d in dests:
                        nfa.add_edge(map1[a], sym, map1[d])
            for a,m in n2.trans.items():
                for sym,dests in m.items():
                    for d in dests:
                        nfa.add_edge(map2[a], sym, map2[d])
            for acc in n1.accepts:
                nfa.add_edge(map1[acc], '', map2[n2.start])
            nfa.start = map1[n1.start]
            nfa.accepts = set(map2[a] for a in n2.accepts)
            stack.append(nfa)
        elif c == '|':
            n2 = stack.pop(); n1 = stack.pop()
            nfa = NFA()
            s = new_state(); f = new_state(); nfa.add_state(s); nfa.add_state(f)
            map1 = {}; map2 = {}
            for st in n1.states:
                ns = new_state(); map1[st] = ns; nfa.add_state(ns)
            for st in n2.states:
                ns = new_state(); map2[st] = ns; nfa.add_state(ns)
            for a,m in n1.trans.items():
                for sym,dests in m.items():
                    for d in dests:
                        nfa.add_edge(map1[a], sym, map1[d])
            for a,m in n2.trans.items():
                for sym,dests in m.items():
                    for d in dests:
                        nfa.add_edge(map2[a], sym, map2[d])
            nfa.add_edge(s, '', map1[n1.start])
            nfa.add_edge(s, '', map2[n2.start])
            for acc in n1.accepts:
                nfa.add_edge(map1[acc], '', f)
            for acc in n2.accepts:
                nfa.add_edge(map2[acc], '', f)
            nfa.start = s; nfa.accepts = {f}
            stack.append(nfa)
        else:
            nfa = NFA()
            s = new_state(); f = new_state()
            nfa.add_edge(s, c, f)
            nfa.start = s; nfa.accepts = {f}
            stack.append(nfa)
    if len(stack) != 1:
        raise ValueError('Invalid regex or postfix conversion')
    return stack[0]

def regex_to_nfa(regex):
    postfix = regex_to_postfix(regex)
    nfa = postfix_to_nfa(postfix)
    return nfa

# helper: epsilon-closure and move
def epsilon_closure(nfa, states):
    stack = list(states)
    res = set(states)
    while stack:
        s = stack.pop()
        for dest in nfa.trans.get(s, {}).get('', set()):
            if dest not in res:
                res.add(dest); stack.append(dest)
    return res

def move(nfa, states, symbol):
    res = set()
    for s in states:
        for dest in nfa.trans.get(s, {}).get(symbol, set()):
            res.add(dest)
    return res

def nfa_to_dot(nfa):
    lines = []
    lines.append(f"start: {nfa.start}")
    lines.append("accepts: " + ",".join(sorted(nfa.accepts)))
    for a,m in nfa.trans.items():
        for sym,dests in m.items():
            for d in dests:
                lines.append(f"{a} -[{sym if sym!='' else 'ε'}]-> {d}")
    return "\\n".join(lines)

def simulate_nfa(nfa, s):
    current = epsilon_closure(nfa, {nfa.start})
    for ch in s:
        current = epsilon_closure(nfa, move(nfa, current, ch))
    return len(current & nfa.accepts) > 0
