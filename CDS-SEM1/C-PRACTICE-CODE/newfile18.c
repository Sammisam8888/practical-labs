#include <stdio.h>
#include<conio.h>
void main()
{clrscr();
//Q. WAP to print multiplication table for the given number using do while loop?
printf("Enter a number :");int a,b=1;
scanf("%d",&a);
printf("The multiplication table of %d is :",a);
do {
    printf("\n%d x %d =",a,b);
    printf("%d",a*b);
    b+=1;} 
    while (b<=10);    
getch();}