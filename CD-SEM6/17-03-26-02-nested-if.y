%{
#include <stdio.h>
#include <stdlib.h>
int yylex();
void yyerror(const char *s);
int nlevel=0;
%}
%token IF STMT
%%
start:ifs {printf("\n valid statement\n");}
;
ifs:IF cond st {nlevel++;}
;
st:simpst
|'{'compst'}'
|ifs
;
simpst:STMT';'
|';'
;
compst:simpst compst
|ifs compst
|simpst
|ifs
;
cond:'('STMT')'
;
%%
int main()
{
    printf("\n enter an expression\n");
    yyparse();
    printf("\n number of levels of nesting=%d\n",nlevel);
    return 0;
}
void yyerror(const char *s)
{
    printf("\n invalid statement\n");
    exit(0);
}
