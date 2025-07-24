#include <stdio.h>
#include<conio.h>
void main()
{clrscr();
int y=1,x;
printf("Enter a number :"); scanf("%d",&x);
while (x>0){
    y*=x;
    x-=1;}
printf ("The factorial of the given number is : %d",y);
getch();}