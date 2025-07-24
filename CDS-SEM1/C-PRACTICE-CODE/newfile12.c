#include <stdio.h>
#include<conio.h>
void main()
{clrscr();
int a,b;
char op;
printf("Enter 2 numbers :");
scanf("%d%d",&a,&b);
printf("Enter the operation to be performed");
scanf("%c",&op);
switch (op){
    case '+':
    printf("%d",a+b);
    break;
    case '-':
    printf("%d",a-b);
    break;
    case '*':
    printf("%d",a*b);
    break;
    case '%':
    switch (b){
        case 0: 
        printf("Divisor 0 error");
        break;
        default :
        printf ("%d",a%b);
    } 
    case '/':
        switch (b){
        case 0: 
        printf("Divisor 0 error");
        break;
        default :
        printf ("%d",a/b);
    break;
    
    } }
getch();}