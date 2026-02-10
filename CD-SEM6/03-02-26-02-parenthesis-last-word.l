%{
%}
space [ ]*
lword ([^ \n\t])+[ ]*\n
%%
{lword} {
    yytext[strlen(yytext)-1]='\0';
    printf("( %s )\n",yytext);
}
{space} {ECHO;}
%%
main(int argc, char * argv[]){
extern FILE *yyin;
yyin=fopen(argv[1],"r");
yylex();
return 0;
}
