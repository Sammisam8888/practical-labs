#include <stdio.h>
#include<conio.h>
void main()
{clrscr();
printf("Enter number of terms in series of 1/2! + 2/3! + 3/4! +......");
int x,i,j,s;
float d=0.0;
scanf("%d",&x);
for (i=1;i<=x;i++)
{s=1;
for (j=1;j<=i+1;j++)
s*=j;
d+=(float)(i/s);}
printf("the sum of the series upto %d terms is %f",x,d);
getch();}