// wap to perform arithematic operations after storing the answers in variables 


#include <stdio.h>
int main(){
	int a,b;
	printf("Enter 2 numbers :");
	scanf("%d %d",&a,&b);
	if (a<b){
		int temp=a;a=b;b=temp;
	}
	float quoteint = (float)a/b;//here type casting is used to get exact float value after division
	int sum = a+b;
	int product = a*b;
	int difference = a-b;
	int remainder = a%b;
	printf("The sum of the numbers is : %d",sum);
	printf("\nThe difference of the numbers is : %d ",difference);
	printf("\nThe product of the numbers is : %d",product);
	printf("\nThe quoteint of the two numbers is : %f ",quoteint);
	printf("\nThe remainder of the two numbers is : %d ",remainder);
	return 0;
}
