//WAP to calculate the sum of  n natural numbers using for loop & average

#include <stdio.h>
int main(){
	int n,i,sum=0;
	printf("Enter the value n upto which sum is to be calculated :"); 
	scanf("%d",&n);
	
	for (i=1;i<=n;i++){
		sum=sum+i;
	}
	printf("The sum of first %d natural numbers is : %d",n,sum);
	float avg= (float)(sum/n);
	printf("\nThe average of %d numbers is : %f\n",n,avg);
	return 0;
}
