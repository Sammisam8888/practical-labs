%{
    #include <stdio.h>
    int vowels = 0;
    int consonants = 0;
%}

%%

[aeiouAEIOU]    { vowels++; }
[a-zA-Z]        { consonants++; }
\n              { return 0; }
.               { ; }

%%

int main(int argc, char *argv[]) {
    printf("Enter a string: ");
    yylex();
    printf("Number of Vowels: %d\n", vowels);
    printf("Number of Consonants: %d\n", consonants);
    return 0;
}
