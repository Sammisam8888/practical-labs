%{
%}
pattern (abc)*
%%
{pattern} {printf("%c",'-');}
%%
main(int argc, char * argv[]){
extern FILE *yyin;
yyin=fopen(argv[1],"r");
yylex();
return 0;
}
