%{
    #include <stdio.h>
    int if_count = 0;
    int max_depth = 0;
    int current_depth = 0;
%}

%%

"if" { if_count++; current_depth++; if (current_depth > max_depth) max_depth = current_depth; }
"}"  { if (current_depth > 0) current_depth--; } 
.    { ; }
\n   { ; }

%%

int main(int argc, char *argv[]) {
    printf("Enter code with nested IF statements (Ctrl+D to end):\n");
    yylex();
    
    printf("\nTotal IF statements: %d\n", if_count);
    printf("Maximum Nesting Level: %d\n", max_depth);
    return 0;
}
