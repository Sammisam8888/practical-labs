%{
    #include <stdio.h>
    int countalpha=0,countdigit=0,countline=0,countspace=0;
%}

alphabet [a-zA-Z]
digit [0-9]
line \n
spaces [ ]
%%
{alphabet} {countalpha++;}
{digit} {countdigit++;}
{line} {countline++;}
{spaces} {countspace++;}
%%
int yywrap() {
    return 1;
}


int main (int argc, char *argv[]){
    extern FILE *yyin;
    yyin = fopen (argv[1],"r");
    yylex();
    printf("Count of : \nAlphabets = %d, Digits = %d, Lines = %d, Spaces = %d\n",countalpha,countdigit,countline, countspace);
    return 0;
}