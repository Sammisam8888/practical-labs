%{
    #include <stdio.h>
    int valid = 1;
    int top = -1;
    int operand = 0;
    int operator = 0;
    int p = 0;
%}

%%

"(" { p++; }
")" { p--; }
[a-zA-Z0-9]+ { operand++; }
"+"|"-"|"*"|"/" { operator++; }
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
    
    if (valid && p == 0 && operand == operator + 1 && operator > 0) {
        printf("Valid Expression\n");
    } else if (valid && p == 0 && operand == 1 && operator == 0) {
        printf("Valid Expression (Single Operand)\n");
    } else {

        printf("Invalid Expression\n");
    }
    return 0;
}
