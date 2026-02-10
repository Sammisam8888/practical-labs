%{
%}
space124 [ ]{1,4}
space528 [ ]{5,8}
%%
{space124} {printf("%c",'-');}
{space528} {printf("%c",'@');}
%%
main(int argc, char * argv[]){
extern FILE *yyin;
yyin=fopen(argv[1],"r");
yylex();
return 0;
}
