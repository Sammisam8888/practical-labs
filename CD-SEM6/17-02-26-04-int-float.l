%{
    #include <stdio.h>
    int int_count = 0;
    int float_count = 0;
%}

%%

[-+]?[0-9]*\.[0-9]+  { printf("%s is a Valid Float\n", yytext); float_count++; }
[-+]?[0-9]+          { printf("%s is a Valid Integer\n", yytext); int_count++; }
\n                   { ; }
.                    { ; }

%%

int main(int argc, char *argv[]) {
    printf("Enter numbers (Ctrl+D to end):\n");
    yylex();
    
    printf("\nTotal Integers: %d\n", int_count);
    printf("Total Floats: %d\n", float_count);
    return 0;
}
