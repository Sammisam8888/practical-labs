%{
#include <stdio.h>
int n = 1;
%}

%%
[^\n]+   { printf("%4d# %s", n++, yytext); }
\n       { printf("\n"); }
%%

int yywrap() {
    return 1;
}

int main(int argc, char *argv[]) {
    extern FILE *yyin;
    yyin = fopen(argv[1], "r");
    yylex();
    return 0;
}
