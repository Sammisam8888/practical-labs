%{
%}
word [^ \n\t]+
rest [ ]*([^\n])+\n
%%
{word} {printf("<%s>",yytext);}
{rest} {ECHO;}
%%
main(int argc, char * argv[]){
extern FILE *yyin;
yyin=fopen(argv[1],"r");
yylex();
return 0;
}
