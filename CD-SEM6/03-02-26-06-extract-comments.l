%{
int flag=0;
%}
comment \/\*.*\*\/
begin \/\*
end \*\/
%%
{comment} {printf("%s :Single line comment",yytext);}
{begin} {printf("%s :Comment begin",yytext);flag=1;}
{end} {printf("%s :Comment close",yytext);flag=0;}
. {if(flag==1) printf("%s",yytext);}
%%
main(int argc, char * argv[]){
extern FILE *yyin;
yyin=fopen(argv[1],"r");
yylex();
return 0;
}
