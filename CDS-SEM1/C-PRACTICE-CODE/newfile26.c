#include <stdio.h>
#include<conio.h>
void main()
{clrscr();
//Q. Enter a number and check whether it is prime number or not?
int n,i,j;
printf("enter a number");
scanf ("%d",&n);
for (i=2;i<=n/2+1 ;i++)
{
if (n%i==0)
{
j=0;
break;}
else
j=1;}

if (j==0)
printf("The number %d is not a prime number",n);
else if (j==1)
printf("The number %d is a prime number",n);
getch();}