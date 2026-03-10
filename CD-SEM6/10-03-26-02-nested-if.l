%{
#include "y.tab.h"
%}
%%
"if" {return IF;}
[ \t]+ { /* ignore */ }
[-+_A-Za-z0-9!=><]+ {return STMT;}
. {return yytext[0];}
\n {return 0;}
%%
int yywrap() { return 1; }
