%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);
%}
%token NUM ID
%left '+' '-'
%left '*' '/'
%nonassoc UMINUS
%%
exp: exp '+' exp
| exp '-' exp
| exp '/' exp
| exp '*' exp
| '-' exp %prec UMINUS
| '(' exp ')'
| NUM
| ID
;
%%
int main()
{
    printf("\n Enter an expression:");
    yyparse();
    printf("\n valid expression\n");
    return 0;
}
void yyerror(const char *s){
    printf("\n Invalid expression\n");
    exit(0);
}
