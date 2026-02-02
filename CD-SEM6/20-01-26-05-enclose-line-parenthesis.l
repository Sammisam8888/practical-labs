%{
#include <stdio.h>
%}

%%
.*\n   { printf("(%s)", yytext); }
.+     { printf("(%s)\n", yytext); }
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
