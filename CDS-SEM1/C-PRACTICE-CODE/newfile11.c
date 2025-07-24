#include <stdio.h>
#include<conio.h>
void main()
{clrscr();
char a;
printf("Enter an alphabet ");
scanf("%c",&a);
switch (a) 
{case 'a' :
case 'e' :
case 'i' :
case 'o' :
case 'u' :
printf ("the character is a vowel"); 
break;
default :
printf("the character is a consonant ");
}
getch();}