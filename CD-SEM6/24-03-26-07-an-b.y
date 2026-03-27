%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);
%}
%token A B
%%
start:tena next
;
next: A next
|B
;
tena: A A A A A A A A A A
;
%%
int main()
{
    printf("\n enter a string of A's followed by B\n");
    printf("for the following grammer a^n b, n>=10\n");
    yyparse();
    printf("valid input\n");
    return 0;
}
void yyerror(const char *s)
{
    printf("\n invalid input\n");
    exit(0);
}
