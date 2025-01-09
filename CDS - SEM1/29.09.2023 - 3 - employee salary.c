/*WAP to calculate salary of a employee given - basic pay, 
HRA - 5% of bp,DA - 20% OF bp, travel allowance - 12% of da 
and total salary = BP+ HRA+TA+DA  	*/


#include <stdio.h>
#define hrap 0.05
#define tap 0.12
#define dap 0.2

void main(){
	int bp;
	float sal,da,hra,ta;
	printf("Enter the basic pay of the employee :");
	scanf("%d",&bp);
	da=dap*bp;
	hra=hrap*bp;
	ta=tap*da;
	sal = bp+hra+da+ta;
	printf("The total salary of the employee is : %f",sal);
}
