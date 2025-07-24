/*WAP to calculate salary of a employee given - basic pay, 
HRA - 5% of bp,DA - 20% OF bp, travel allowance - 12% of bp 
and total salary = BP+ HRA+TA+DA  	*/
#include <stdio.h>
void main(){
	int bp;
	float sal,da,hra,ta;
	printf("Enter the basic pay of the employee :");
	scanf("%d",&bp);
	da=0.2*bp;
	hra=0.05*bp;
	ta=0.12*bp;
	sal = bp+hra+da+ta;
	printf("The total salary of the employee is : %f",sal);
	
	
}