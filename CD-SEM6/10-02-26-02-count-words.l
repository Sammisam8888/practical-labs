%{
    #include <stdio.h>
    int countword=0;
%}
word [^\t\n]+
%%
{word} {countword++;}
%%
int yywrap() {
    return 1;
}


int main (int argc, char *argv[]){
    extern FILE *yyin;
    yyin = fopen (argv[1],"r");
    yylex();
    printf("Count of Words = %d\n", countword);
    return 0;
}