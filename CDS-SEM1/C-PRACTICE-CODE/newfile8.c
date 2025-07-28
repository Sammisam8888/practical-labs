#include <stdio.h>
#include<conio.h>
void main()
{clrscr();
printf("Enter a digit :");
int a;
scanf("%d",&a);
switch(a){
    case 0:
    goto c;
    break;
    case 1:
    goto c;
    break;
    default: 
    printf ("%d is an integer digit",a);}
c:
printf("%d is a binary digit",a);

getch();}