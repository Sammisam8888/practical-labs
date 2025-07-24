//Multiplication of n numbers using recursion

#include <stdio.h>
int h=1;
int mul(){
     int k;
     printf("Enter a number to be multiplied (enter 0 to stop) :");
     scanf("%d",&k);
     if (k==0){
         return 1;
     }
     else {
         h*=mul();
         return k;}
}
         
void main()
{
    int g=mul();
    printf("Product = %d",g);
}