#include <stdio.h>
#include<conio.h>
void main()
{clrscr();
//Write an array which takes in roll no and marks in 3 subjects for 10 students. Print the roll no, total marks and average for all students.
int a[10],b[10],c[10],d[10],i;
float e[10];
for (i=0;i<10;i++)
{printf ("Enter roll no :");
scanf("%d",&d[i]);
printf ("Enter marks in 3 subjects :");
scanf("%d%d%d",&a[i],&b[i],&c[i]);
e[i] =(float)((a[i]+b[i]+c[i])/3);}
for (i=0;i<10;i++)
printf("The roll number is %d & the average mark is %f",a[i], e[i]);
getch();}