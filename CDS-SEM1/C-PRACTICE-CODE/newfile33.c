#include <stdio.h>
#include<conio.h>
#define r 3
#define c 2
void main()
{clrscr();
int a[r][c],b[r][c],i,j;
printf("Enter the data in first Matrix : \n");
for (i=0;i<r;i++)
{for (j=0;j<c;j++)
scanf("%d",&a[i][j]);
}
for (i=0;i<r;i++)
{for (j=0;j<c;j++)
b[i][j]=a[i][j];
}
printf("Transpose of matrix is :\n");
for(i=0;i<r;i++)
{for (j=0;j<c;j++)
{
printf(" %d ",b[i][j]);}
printf("\n");}
getch();}