//WAP to enter 2 numbers and perform all arithematic operations on it

#include <stdio.h>
int main(){
	int a,b;
	printf("Enter 2 numbers :");
	scanf("%d %d",&a,&b);
	if (a<b){
		int temp=a;a=b;b=temp;
	}
	float quoteint = (float)a/b;//here type casting is used to get exact float value after division
	printf("The sum of the numbers is : %d",a+b);
	printf("\nThe difference of the numbers is : %d",a-b);
	printf("\nThe product of the numbers is : %d",a*b);
	printf("\nThe quoteint of the two numbers is : %f ",quoteint);
	printf("\nThe remainder of the two numbers is : %d ",a%b);
	return 0;
}
