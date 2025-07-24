
/* q - print structure
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
*/  
#include <stdio.h>


int main()
{
for (int i=0;i<5;i++){
for (int j=0;j<5;j++){
if (j>=i)
printf("* ");
else printf("  ");}
for(int k=0;k<4;k++){
if (k>=i) printf ("* ");}
printf("\n");}
    
return 0;
}