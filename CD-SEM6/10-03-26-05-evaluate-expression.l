%{
#include "y.tab.h"
#include <stdlib.h>
%}
%%
([0-9]+|[0-9]*\.[0-9]+)+ {yylval.fval=atof(yytext);return NUM;}
. return yytext[0];
\n return 0;
%%
int yywrap() { return 1; }
