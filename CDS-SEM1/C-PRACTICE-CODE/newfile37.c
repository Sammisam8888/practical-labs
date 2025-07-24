#include <stdio.h>
#include<conio.h>
#include <string.h>
void main()
{clrscr();
//Q. count number of words in a string & number of letters
char s[40];
int i,j=1,k=0;
printf("Enter a string :");
gets(s);
for(i=0;s[i]!='\0';i++)
{if (s[i]==' ')
j++;
else
k++;}
printf("The number of words in string %s is : %d",s,j);
printf ("\nAnd the number of letters are %d :",k);
getch();}