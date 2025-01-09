//wap to calculate simple interest and compound interest 

#include<stdio.h>
#include<math.h>
void main(){
	float p,r,t;
	printf("Enter principal, rate and time :");
	scanf("%f%f%f",&p,&r,&t);
	float si=(float)(p*r*t/100);
	float ci =p*pow(1+(float)(r/100),t)-p; 		//instead of pow func, we can use a^b
	printf("The simple interest on the given amount and interest rate is : %f\n",si);
	printf("The compound interest on the given amount and interest rate is : %f\n",ci);
		
}
