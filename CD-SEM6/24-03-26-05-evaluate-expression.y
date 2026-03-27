%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);
%}
%union {float fval;}
%token <fval> NUM
%type <fval> e
%type <fval> start
%left '+' '-'
%left '*' '/'
%nonassoc UMINUS
%%
start:e {printf("=%2.2f\n",$1);}
;
e:e '+' e {$$=$1+$3;}
|e '-' e {$$=$1-$3;}
|e '*' e {$$=$1*$3;}
|e '/' e {
    if($3==0) {
        yyerror("divided by zero");
    } else {
        $$=$1/$3;
    }
}
|'-' e %prec UMINUS {$$=-$2;}
|'(' e ')' {$$=$2;}
|NUM {$$=$1;}
;
%%
int main()
{
    printf("\n enter aritmetic expression\n");
    yyparse();
    printf("\n valid expression\n");
    return 0;
}
void yyerror(const char *s)
{
    printf("\n invalid expression: %s\n", s);
    exit(0);
}
