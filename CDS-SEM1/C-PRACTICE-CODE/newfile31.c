#include <stdio.h>
#include<conio.h>
void main()
{clrscr();
//Q. Enter a 10 numbers and sort them in ascending order?
int n,d;
printf("Enter the number of elements in array :");
scanf("%d",&n);
int a[n],i,j;
for (i=0;i<n;i++)
{printf("Enter %d no:",++i);scanf("%d",&a[--i]);}
for (i=0;i<n;i++)
{for (j=i;j<n;j++)
{if (a[i]>a[j])
{int s=a[i];
a[i]=a[j];
a[j]=s;}}}
printf("the array in  ascending order is :");
for (i=0;i<n;i++)
printf("\n%d",a[i]);
getch();}