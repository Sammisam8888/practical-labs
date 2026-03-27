%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);
%}
%token VAR
%%
start:VAR
|
;
%%
int main()
{
    printf("\n enter a variable\n");
    yyparse();
    printf("\n valid variable\n");
    return 0;
}
void yyerror(const char *s)
{
    printf("\n invalid variable\n");
    exit(0);
}
