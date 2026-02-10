%{
%}
pattern1 [a-k]
pattern2 [3-6]
%%
{pattern1} {printf("%c",'*');}
{pattern2} {printf("%c",'~');}
%%
main(int argc, char * argv[]){
extern FILE *yyin;
yyin=fopen(argv[1],"r");
yylex();
return 0;
}
