#include<stdio.h>
#include<math.h>
void main(){
	float p,r,t;
	printf("Enter principal,rate and time :");
	scanf("%f%f%f",&p,&r,&t);
	float si=p*r*t/100;
	float ci =p+pow(1+r/100,t);
	printf("The simple interest on the given amount and interest rate is : %f\n",si);
	printf("The compound interest on the given amount and interest rate is : %f\n",ci);
		
}