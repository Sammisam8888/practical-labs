%{
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

char *keywords[] = {
    "auto","break","case","char","const","continue","default",
    "do","double","else","enum","extern","float","for","goto","if",
    "int","long","register","return","short","signed","sizeof","static",
    "struct","switch","typedef","union","unsigned","void","volatile",
    "while"
};

bool isKeyword(char *s) {
    for (int i = 0; i < 32; i++) {
        if (strcmp(s, keywords[i]) == 0)
            return true;
    }
    return false;
}
%}

%%
[a-zA-Z_][a-zA-Z0-9_]* {
    if (isKeyword(yytext))
        printf("%s : NOT a valid identifier (keyword)\n", yytext);
    else
        printf("%s : valid identifier\n", yytext);
}

.|\n    { /* ignore */ }
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
