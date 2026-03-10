%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);
%}
%token NUM
%left '+' '-'
%left '*' '/'
%nonassoc UMINUS
%%
exp : exp '+' exp
| exp '-' exp
| exp '/' exp
| '-' exp %prec UMINUS
| exp '*' exp
| '(' exp ')'
| NUM
;
%%
int main()
{
    printf("\n Enter an arithmatic expression:\n");
    yyparse();
    printf("\n Valid expression\n");
    return 0;
}
void yyerror(const char *s){
    printf("\n Invalid expression\n");
    exit(0);
}
