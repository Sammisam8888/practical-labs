#include <stdio.h>
#include<conio.h>
void main()
{clrscr();
//Q. Enter 10 elements from the keyboard and display using array?
int a[10],i;
for (i=0;i<10;i++)
{printf("Enter %d th number :",++i);
scanf ("%d",&a[--i]);}
printf("\nThe numbers are");
for (i=0;i<10;i++)
printf("\n%d",a[i]);
getch();}