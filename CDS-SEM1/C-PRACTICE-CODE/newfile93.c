//Q14 - calculator
#include <stdio.h>
int sum(int a, int b){
    return a+b;}
int diff(int a, int b){
    if (a<b)
        return a-b;
    else return b-a;}
int prod(int a,int b){
    return a*b;}
float div(int a,int b){
    return (float)(a/b);}
float rem(int a,int b){
    return a%b;}
 
void main()
{
int a,b,n;
printf("Enter 2 numbers : ");
scanf("%d%d",&a,&b);
while (true) {
printf("\n\nEnter the operation you want to execute on calculator :\n1=add, 2=difference, 3=product, 4=quotient, 5=remainder,6=Exit calculator\n");
scanf("%d",&n);
switch (n){
    case 1:
    printf("The sum is : %d",sum(a,b));
   case 2:
    printf("The difference  is : %d",diff(a,b));
   case 3:
    printf("The product is : %d",prod(a,b));
   case 4:
    printf("The quotiet is : %d",div(a,b));
   case 5:
    printf("The remiander after divisionis : %d",rem(a,b));
   case 6:
    break;
}}               
}