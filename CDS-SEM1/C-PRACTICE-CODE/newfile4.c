// sizeof() operator uses
#include <stdio.h>
#include<conio.h>
void main()
{clrscr();
printf(" void %d", sizeof(void()));
printf("\n empty string %d", sizeof(""));
printf("\n int %d", sizeof(int));
printf("\n char %d", sizeof(char));
printf("\n 4.34 double %d", sizeof(4.34));
printf("\n 4.34 float %d", sizeof(4.34f));
printf("\n constant 58 -  %d", sizeof(58));
printf("\n string constant abc - %d", sizeof("abc"));
printf("\n string a - %d", sizeof("a"));
printf("\n char a - %d", sizeof('a'));
printf("\n string ab - %d", sizeof('ab'));

getch();}
