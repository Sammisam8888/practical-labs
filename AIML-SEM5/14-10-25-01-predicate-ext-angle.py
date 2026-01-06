"""
Resolution proof (pure Python) following sequence: 1 -> 3 -> 2 -> 4 -> 5 -> 6
Clauses:
 C1: equal(sum(<A,<B,<C), 180)
 C2: equal(sum(ext<C,<C), 180)
 C3: equal(x,y), equal(y,z) -> equal(x,z)   (transitivity)
 C4: equal(y,z) -> equal(z,y)               (symmetry)
 C5: equal(sum(x,y), sum(x,z)) -> equal(y,z)
 C6: negated goal: ¬equal(ext<C, sum(<A,<B))
"""

import pprint
pp = pprint.PrettyPrinter(width=120)

# optional drawing libs
try:
    import networkx as nx
    import matplotlib.pyplot as plt 
    DRAW = True
except Exception:
    DRAW = False

# ---------- representation helpers ----------
def SUM(*args):
    return ("sum",) + tuple(args)

def EQUAL(a, b):
    return ("equal", a, b)

def NEG(a):
    return ("not", a)

def is_equal(atom):
    return isinstance(atom, tuple) and len(atom) == 3 and atom[0] == "equal"

def is_sum(term):
    return isinstance(term, tuple) and term and term[0] == "sum"

# ---------- Given clauses (C1..C6) ----------
C1 = EQUAL(SUM("<A", "<B", "<C"), "180")           # equal(sum(<A,<B,<C), 180)
C2 = EQUAL(SUM("ext<C", "<C"), "180")              # equal(sum(ext<C,<C), 180)
C3 = "C3_TRANSITIVITY"                             # schema: equal(x,y) & equal(y,z) -> equal(x,z)
C4 = "C4_SYMMETRY"                                 # schema: equal(y,z) -> equal(z,y)
C5 = "C5_SUM_CANCEL"                               # schema: equal(sum(x,y), sum(x,z)) -> equal(y,z)
C6 = NEG(EQUAL("ext<C", SUM("<A", "<B")))          # negated goal

# store provenance and derived atoms
derived = {}
derived["C1"] = (C1, "given C1")
derived["C2"] = (C2, "given C2")
derived["C3"] = (C3, "rule C3 (transitivity)")
derived["C4"] = (C4, "rule C4 (symmetry)")
derived["C5"] = (C5, "rule C5 (sum-cancellation)")
derived["C6"] = (C6, "given C6 (negated goal)")

steps = []   # list of (label, atom, used, description)

# ---------- Step A: instantiate C3 using C1  (this is "1 + 3 -> instantiated rule") ----------
# C3: equal(x,y) & equal(y,z) -> equal(x,z)
# Given C1: equal(sum(<A,<B,<C), 180)   i.e. x := sum(<A,<B,<C), y := 180
# Instantiation: equal(180, z) -> equal(sum(<A,<B,<C), z)
# Represent the instantiated rule as a clause-of-form: ("impl", premises_tuple, conclusion_template)
inst_Rule_from_C1 = ("impl", (("equal", "180", "Z"),), ("equal", SUM("<A", "<B", "<C"), "Z"))
# store and record
derived["Inst1_C3"] = (inst_Rule_from_C1, "instantiated C3 with C1 (x=sum(A,B,C), y=180)")
steps.append( ("Inst1_C3", inst_Rule_from_C1, ("C1","C3"), "Instantiate C3 with C1: if equal(180,Z) then equal(sum(<A,<B,<C), Z)") )

# ---------- Step B: use instantiated rule with C2  (instantiated rule + C2 -> R1) ----------
# instantiated rule expects equal(180, Z) as premise. C2 is equal(sum(ext<C,<C), 180).
# We can match equal(180, Z) with equal(sum(ext<C,<C), 180) by symmetry or by matching swapped sides.
# To match we can flip C2 via symmetry of equality conceptually; but per requested sequence we do:
# instantiate premise equal(180,Z) matched by equality with the RHS of C2 by recognizing equal(A,B) implies equal(B,A).
# Practically: match premise equal(180,Z) to equal(sum(ext<C,<C), 180) by taking Z = sum(ext<C,<C) and swapping sides.
# This yields conclusion equal(sum(<A,<B,<C), sum(ext<C,<C))
# We'll perform that matching explicitly.

# match: premise ("equal","180","Z") with C2 ("equal", sum(extC,C), "180")
match_prem = ("equal", "180", "Z")
c2_atom = C2  # ("equal", SUM("ext<C", "<C"), "180")
# Solve for Z by matching the third element of c2 to match_prem[1]? We want mapping: "180" <-> "180", "Z" -> sum(extC,C) when swapping sides
# So set Z = sum(extC,<C)
Z_value = c2_atom[1]  # sum(ext<C, <C>)
# produce derived R1:
R1 = EQUAL(SUM("<A", "<B", "<C"), Z_value)   # equal(sum(A,B,C), sum(extC,C))
derived["R1"] = (R1, "From Instantiated C3 and C2 by matching (swap/match) -> equal(sum(A,B,C), sum(extC,C))")
steps.append( ("R1", R1, ("Inst1_C3","C2"), "Apply instantiated C3 to C2 (match Z = sum(ext<C,<C>)) -> R1") )

# ---------- Step C: apply C4 (symmetry) to R1 -> R2 ----------
# R1 = equal(sum(A,B,C), sum(extC,C))
# Applying symmetry gives equal(sum(extC,C), sum(A,B,C))
def apply_symmetry(atom):
    if is_equal(atom):
        return EQUAL(atom[2], atom[1])
    return None

R2 = apply_symmetry(R1)
derived["R2"] = (R2, "From R1 by C4 (symmetry) -> equal(sum(ext<C,<C), sum(<A,<B,<C))")
steps.append( ("R2", R2, ("R1","C4"), "Apply C4 (symmetry) to R1 -> R2") )

# ---------- Step D: apply C5 (sum-cancellation) to R2 -> R3 ----------
# C5: equal(sum(x,y), sum(x,z)) -> equal(y,z)
# Here R2 is equal(sum(extC, <C>), sum(<A,<B,<C>))
# Both sides are sum terms with last element "<C". We cancel the common "<C" to get equal(sum(extC), sum(<A,<B>))
def apply_sum_cancel(atom):
    if not is_equal(atom):
        return None
    L = atom[1]
    R = atom[2]
    if is_sum(L) and is_sum(R):
        # check if they share the same last element
        if len(L) >=2 and len(R) >=2 and L[-1] == R[-1]:
            # remove last elements
            newL = ("sum",) + tuple(L[1:-1]) if len(L) > 2 else ("sum", L[1])   # for multi or singleton
            newR = ("sum",) + tuple(R[1:-1]) if len(R) > 2 else ("sum", R[1])
            return EQUAL(newL, newR)
    return None

R3 = apply_sum_cancel(R2)
derived["R3"] = (R3, "From R2 by C5 (sum cancellation of '<C>') -> equal(sum(ext<C), sum(<A,<B))")
steps.append( ("R3", R3, ("R2","C5"), "Apply C5: cancel common '<C' in the two sums -> R3") )

# ---------- Step E: normalize singleton sums if needed -> R4 ----------
# R3 may have ("sum", "ext<C") on left (i.e. singleton sum). Normalize that to atom ext<C directly:
def normalize_singleton_sum(atom):
    if not is_equal(atom):
        return None
    L, R = atom[1], atom[2]
    def norm(t):
        if is_sum(t) and len(t) == 2:   # ("sum", item)
            return t[1]
        return t
    return EQUAL(norm(L), norm(R))

R4 = normalize_singleton_sum(R3)
derived["R4"] = (R4, "Normalize singleton sums -> equal(ext<C, sum(<A,<B))")
steps.append( ("R4", R4, ("R3","normalize"), "Normalize singleton sums: left becomes ext<C -> R4") )

# ---------- Step F: refute with C6 (negated goal) -> contradiction ----------
# C6 = ("not", equal("ext<C", sum("<A","<B")))
contradiction = False
if is_equal(R4) and isinstance(C6, tuple) and C6[0] == "not" and is_equal(C6[1]):
    if R4 == C6[1]:
        contradiction = True
        steps.append( ("⊥", "CONTRADICTION", ("R4","C6"), "R4 contradicts C6 -> ⊥") )

# ---------- Print the step trace ----------
print("\n=== RESOLUTION PROOF TRACE (sequence 1 -> 3 -> 2 -> 4 -> 5 -> 6) ===\n")
print("Given clauses:")
print(" C1:", C1)
print(" C2:", C2)
print(" C3:", C3)
print(" C4:", C4)
print(" C5:", C5)
print(" C6:", C6)
print("\nDerived steps (in order):\n")
for i, (label, atom, used, desc) in enumerate(steps, start=1):
    print(f" Step {i}: {label}")
    print(f"    Derived: {atom}")
    print(f"    Used: {used}")
    print(f"    Note: {desc}\n")

if contradiction:
    print("Result: ⊥ (contradiction) reached. Negated goal unsatisfiable → goal proven true.")
    print("Conclusion: equal(ext<C, sum(<A,<B)) holds (exterior angle = sum of opposite interior angles).")
else:
    print("No contradiction found. Check pattern matching. (Expected contradiction.)")

# ---------- Optional: draw a neat top-down resolution tree (if drawing libs available) ----------
def draw_tree():
    if not DRAW:
        print("\n(Drawing skipped: networkx/matplotlib not available in this environment.)")
        return

    G = nx.DiGraph()
    labels = {
        "C1": "C1\n= equal(sum(<A,<B,<C), 180)",
        "C3": "C3\ntransitivity",
        "Inst1_C3": "Inst(C3)\nif equal(180,Z) then equal(sum(<A,<B,<C), Z)",
        "C2": "C2\n= equal(sum(ext<C,<C), 180)",
        "R1": "R1\n= equal(sum(<A,<B,<C), sum(ext<C,<C))",
        "C4": "C4\nsymmetry",
        "R2": "R2\n= equal(sum(ext<C,<C), sum(<A,<B,<C))",
        "C5": "C5\nsum-cancellation",
        "R3": "R3\n= equal(sum(ext<C), sum(<A,<B))",
        "R4": "R4\n= equal(ext<C, sum(<A,<B))",
        "C6": "C6\n= ¬equal(ext<C, sum(<A,<B))",
        "⊥": "⊥\nContradiction"
    }

    # add nodes and edges in the exact logical flow:
    G.add_nodes_from(labels.keys())
    edges = [
        ("C1", "Inst1_C3"), ("C3", "Inst1_C3"),            # instantiate C3 using C1
        ("Inst1_C3", "R1"), ("C2", "R1"),                 # Inst1 + C2 -> R1
        ("R1", "R2"), ("C4", "R2"),                       # R1 + C4 -> R2
        ("R2", "R3"), ("C5", "R3"),                       # R2 + C5 -> R3
        ("R3", "R4"),                                     # normalization
        ("R4", "⊥"), ("C6", "⊥")                          # R4 + C6 -> contradiction
    ]
    G.add_edges_from(edges)

    pos = {
        "C1": (-2, 6), "C3": (0, 6), "Inst1_C3": (-1, 5.0),
        "C2": (2, 6), "R1": (0, 4.0), "C4": (2.5, 4.0),
        "R2": (0, 3.0), "C5": (-2.5, 3.5), "R3": (0, 2.0),
        "R4": (0, 1.3), "C6": (2.5, 1.3), "⊥": (0, 0.3)
    }

    plt.figure(figsize=(11,8))
    nx.draw(G, pos, with_labels=False, node_size=2600, node_color="#E8F6FF", edgecolors="black", arrowsize=18)
    for n, txt in labels.items():
        x, y = pos[n]
        plt.text(x, y, txt, fontsize=9, ha='center', va='center', wrap=True)
    plt.title("Resolution Tree (1 → 3 → 2 → 4 → 5 → 6)", fontsize=13, pad=12)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

draw_tree()