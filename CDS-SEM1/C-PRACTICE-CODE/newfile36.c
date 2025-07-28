#include <stdio.h>
#include<conio.h>
void main()
{clrscr();
char s[20],r[20];
printf("Enter a string :");
gets(s);
int l=0,i;
while (s[l]!='\0')
l++;
for (i=0;i<l;i++)
r[i]=s[l-1-i];
r[l]='\0';
printf ("Reverse of string %s is : %s",s,r);
getch();}