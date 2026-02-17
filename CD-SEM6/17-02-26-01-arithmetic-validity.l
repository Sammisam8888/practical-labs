%{
    #include <stdio.h>
    int valid = 1;
    int top = -1;
    int operand_count = 0;
    int operator_count = 0;
    int p_balance = 0;
%}

%%

"(" { p_balance++; }
")" { p_balance--; }
[a-zA-Z0-9]+ { operand_count++; }
"+"|"-"|"*"|"/" { operator_count++; }
\n { return 0; }
. { valid = 0; }

%%

int main(int argc, char *argv[]) {
    printf("Enter an arithmetic expression: ");
    yylex();
    
    // Check validity logic
    // 1. Parentheses must be balanced
    // 2. Operands should be exactly Operator + 1 (for binary operators)
    // 3. No invalid characters found
    
    if (valid && p_balance == 0 && operand_count == operator_count + 1 && operator_count > 0) {
        printf("Valid Expression\n");
    } else if (valid && p_balance == 0 && operand_count == 1 && operator_count == 0) {
        printf("Valid Expression (Single Operand)\n");
    } else {
        printf("Invalid Expression\n");
        // Debug info if needed:
        // printf("Debug: Ops=%d, Oprnds=%d, P_Bal=%d\n", operator_count, operand_count, p_balance);
    }
    return 0;
}
