#include <stdio.h>
int main(){
	printf("Enter the details for finding simple and compound interest : \nEnter principal amount :";
	int principal; float time,interest,si,ci;
	scanf("%d",principal);
	printf("Enter the interest rate (in %) :");
	scanf("%d",interest);
	printf("Enter the time (in years) :");
	scanf("%f",time);
	si=(float)p*r*t/100;
	printf("The simple interest on the principal amount is : %f",si);
//	printf("The compound interest on the principal amount is : %f",ci);	
}