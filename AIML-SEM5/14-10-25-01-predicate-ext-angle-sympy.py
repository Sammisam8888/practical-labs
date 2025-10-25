"""
take the triangle 
it has 3 angles
the sum of the angles is 180 degrees
prove that the exterior angle is equal to the sum of the two interior opposite angles
let the triangle be ABC
let the angle be ext (C)

given assumptions : C + ext (C) = 180 (linear pair)
given data: A + B + C = 180 (triangle sum)
to prove: ext (C) = A + B
"""

"""import sympy as sp
A,B,C,extC=sp.symbols('A B C extC')


def equal(p, q):
    return sp.Eq(p, q)

def implies(p, q):
    return sp.Implies(p, q)

def negative(p):
    return sp.Not(p)
def extangle():
    eq1 = equal(A + B + C, 180)
    eq2 = equal(C + extC, 180)
    axiom1 = implies(equal(A, B) & equal(B,C), equal(A, C))
    axiom2 = implies(equal(A,B),equal(B,A))
    goal = equal(extC, A + B)
    S=set()
    S.add(eq1)
    S.add(eq2)
    S.add(axiom1)
    S.add(axiom2)
    S.add(negative(goal))
    return S
"""


import sympy

# -- Part 1: A Class to Represent Symbolic Literals --
# This class wraps SymPy expressions (Eq, Ne) to handle negation.

class SymbolicLiteral:
    """Represents a logical literal using a SymPy expression (Eq or Ne)."""
    def __init__(self, expression):
        if not isinstance(expression, (sympy.Eq, sympy.Ne)):
            raise TypeError("SymbolicLiteral must be initialized with a sympy Eq or Ne object.")
        self.expression = expression

    def __repr__(self):
        """String representation for printing."""
        return str(self.expression)

    def __eq__(self, other):
        """Two literals are equal if their expressions are."""
        return isinstance(other, SymbolicLiteral) and self.expression.equals(other.expression)

    def __hash__(self):
        """To allow literals to be stored in sets (clauses)."""
        return hash(self.expression)

    def negate(self):
        """Returns the negation of this literal."""
        if isinstance(self.expression, sympy.Eq):
            # The negation of Eq(a, b) is Ne(a, b)
            return SymbolicLiteral(sympy.Ne(self.expression.lhs, self.expression.rhs))
        elif isinstance(self.expression, sympy.Ne):
            # The negation of Ne(a, b) is Eq(a, b)
            return SymbolicLiteral(sympy.Eq(self.expression.lhs, self.expression.rhs))

# -- Part 2: Explicit CNF Conversion Function --
# This function demonstrates the conversion of implications to CNF.

def implication_to_cnf(implication):
    """
    Converts a SymPy Implies object into a CNF clause (a set of SymbolicLiterals).
    Handles implications of the form (P & Q & ...) -> R.
    
    Rule: (A -> B) is equivalent to (~A v B)
    Rule: ~(A & B) is equivalent to (~A v ~B) [De Morgan's Law]
    """
    if not isinstance(implication, sympy.logic.boolalg.Implies):
        raise TypeError("Input must be a sympy Implies object.")

    antecedent = implication.args[0]
    consequent = implication.args[1]

    # The resulting clause is (~antecedent V consequent)
    # We apply De Morgan's laws if the antecedent is an And(...)
    
    clause_literals = set()
    
    # Add the negated literals from the antecedent
    if isinstance(antecedent, sympy.logic.boolalg.And):
        # Antecedent is P & Q & ...
        # Negating it gives ~P v ~Q v ...
        for arg in antecedent.args:
            clause_literals.add(SymbolicLiteral(arg).negate())
    else:
        # Antecedent is a single predicate P
        # Negating it gives ~P
        clause_literals.add(SymbolicLiteral(antecedent).negate())
        
    # Add the positive literal from the consequent
    clause_literals.add(SymbolicLiteral(consequent))
    
    return frozenset(clause_literals)

# -- Part 3: The Resolution Prover (using SymPy literals) --

class ResolutionProver:
    def __init__(self, initial_clauses):
        self.clauses = [frozenset(c) for c in initial_clauses]
        self.generated = set(self.clauses)

    def run(self):
        """
        Runs the resolution algorithm, printing each step.
        """
        print(f"{'Step':<5} | {'Clause 1':<45} | {'Clause 2':<45} | {'Resolvent (New Clause)'}")
        print("-" * 110)
        
        step_num = 0
        while True:
            new_clauses = set()
            clauses_list = list(self.generated) # Use a snapshot for stable iteration
            
            for i in range(len(clauses_list)):
                for j in range(i, len(clauses_list)):
                    clause1 = clauses_list[i]
                    clause2 = clauses_list[j]
                    
                    resolvent = self.resolve(clause1, clause2)

                    if resolvent is not None and resolvent not in self.generated:
                        step_num += 1
                        print_step(step_num, clause1, clause2, resolvent)
                        
                        if not resolvent: # Empty clause means contradiction
                            print("\n" + "="*110)
                            print("CONCLUSION: Contradiction found (Empty Clause {} generated).")
                            print("The negated goal is false, therefore the original goal is TRUE.")
                            print("Q.E.D. The theorem is proven.")
                            print("="*110)
                            return True
                        
                        new_clauses.add(resolvent)
            
            if not new_clauses:
                print("\n" + "="*110)
                print("CONCLUSION: No new clauses can be generated and no contradiction was found.")
                print("The goal cannot be proven from the given axioms.")
                print("="*110)
                return False

            self.generated.update(new_clauses)

    def resolve(self, clause1, clause2):
        """
        Attempts to resolve two clauses of SymbolicLiterals.
        """
        for literal1 in clause1:
            if literal1.negate() in clause2:
                temp_c1 = set(clause1)
                temp_c2 = set(clause2)
                temp_c1.remove(literal1)
                temp_c2.remove(literal1.negate())
                return frozenset(temp_c1.union(temp_c2))
        return None

# -- Part 4: Helper function for Visual Display --

def format_clause_sympy(clause):
    if not clause:
        return "{}"
    # Using sorted with a key to make the output deterministic and clean
    return "{" + " v ".join(sorted([str(l) for l in clause], key=len)) + "}"

def print_step(step_num, c1, c2, resolvent):
    c1_str = format_clause_sympy(c1)
    c2_str = format_clause_sympy(c2)
    res_str = format_clause_sympy(resolvent)
    print(f"{step_num:<5} | {c1_str:<45} | {c2_str:<45} | {res_str}")

# -- Part 5: Main Execution --

if __name__ == "__main__":
    # --- 1. Define Symbols and Predicates using SymPy ---
    A, B, C, ext_C, x, y, z = sympy.symbols('A B C ext_C x y z')
    
    # Predicates are the fundamental equations
    p = sympy.Eq(A + B + C, 180)
    q = sympy.Eq(ext_C + C, 180)
    r = sympy.Eq(A + B + C, ext_C + C) # Consequence of transitivity
    s = sympy.Eq(A + B, ext_C)         # Goal and consequence of simplification

    print("="*110)
    print(" AUTOMATED THEOREM PROVING WITH SYMPY AND RESOLUTION ".center(110))
    print("="*110)
    
    # --- 2. Define Axioms as Logical Implications ---
    # Axiom 3: Transitivity of Equality. (p & q) => r
    axiom3_implication = sympy.Implies(sympy.And(p, q), r)
    # Axiom 4: Algebraic Simplification. r => s
    axiom4_implication = sympy.Implies(r, s)

    print("Defined Axioms as Implications:")
    print(f"  Axiom 3 (Transitivity): {axiom3_implication}")
    print(f"  Axiom 4 (Simplification): {axiom4_implication}\n")

    # --- 3. Convert Implications to CNF Clauses ---
    clause3 = implication_to_cnf(axiom3_implication)
    clause4 = implication_to_cnf(axiom4_implication)

    print("Converting Implications to CNF Clauses:")
    print(f"  Axiom 3 becomes: {format_clause_sympy(clause3)}")
    print(f"  Axiom 4 becomes: {format_clause_sympy(clause4)}\n")

    # --- 4. Assemble the Initial Knowledge Base (Set S) ---
    initial_knowledge_base = [
        frozenset({SymbolicLiteral(p)}),              # Axiom 1: A+B+C = 180
        frozenset({SymbolicLiteral(q)}),              # Axiom 2: ext_C+C = 180
        clause3,                                      # Axiom 3 in CNF
        clause4,                                      # Axiom 4 in CNF
        frozenset({SymbolicLiteral(s).negate()})      # Negated Goal: A+B != ext_C
    ]
    
    print("Initial Knowledge Base (Set S) for Resolution:")
    for i, clause in enumerate(initial_knowledge_base):
        print(f"  Clause {i+1}: {format_clause_sympy(clause)}")
    print("\nStarting Resolution...\n")

    # --- 5. Run the Prover ---
    prover = ResolutionProver(initial_knowledge_base)
    prover.run()