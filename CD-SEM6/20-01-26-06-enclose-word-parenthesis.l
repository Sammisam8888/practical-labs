%{
#include <stdio.h>
%}

%%
[^\t\n ]+   { printf("(%s)", yytext); }
[ \t\n]+    { printf("%s", yytext); }
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
