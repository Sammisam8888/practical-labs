#include <stdio.h>
#include<conio.h>
void main()
{clrscr();
int z=1;
printf("The multiples of both 3 & 5 are below 100 :");
while (z<=100){
    
    if ((z%3==0) && (z%5==0)) 
    printf ("\n%d",z);
    
 

  z+=1;}
getch();}