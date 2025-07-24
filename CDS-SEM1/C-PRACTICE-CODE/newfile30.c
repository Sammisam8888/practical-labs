#include <stdio.h>
#include<conio.h>
void main()
{clrscr();
//Q. Enter an array of 5 elements and copy it to another array?
int a [5],b[5],i;
for (i=0;i<5;)
{printf("Enter a number :");
scanf ("%d",&a[i++]);}
for (i=0;i<5;i++)
b[i]=a[i];

printf("The numbers stored in array : %d,%d,%d,%d,%d ",b[0],b[1],b[2],b[3],b[4]);
getch();}