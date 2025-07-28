#include <stdio.h>
#include<conio.h>
#define a 3
void main()
{clrscr();
int i,j;

int m[a][a]={{3,4,5},{6,7,8},{3,2,1}};
printf("\nThe upper triangular Matrix is :\n");
for(i=0;i<a;i++)
{for (j=0;j<a;j++)
{if (j>=i)
printf(" %d ",m[i][j]);
else
printf ("   ");}
printf("\n");}
getch();}