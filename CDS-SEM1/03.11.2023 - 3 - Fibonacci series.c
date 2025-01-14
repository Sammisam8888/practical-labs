//WAP to print fibonacci series 
#include <stdio.h>
void main(){
	int a=0,b=1,n,i,c;
	printf("Enter the number of elements of fibonacci required :");
	scanf("%d",&n);
	printf("The fibonacci series is : ");
	if (n<=2){
		switch(n){
			case 2:
				printf("%d, %d",a,b);	break;
			case 1 :
				printf("%d ",a);	break;
			default :
				printf("Sorry the value is less than 1");
		}
	}
	else{
	printf("%d, %d",a,b);
		for (i=0;i<n-2;i++){
			c=b; b+=a; a=c;
			printf(", %d",b);
			
		}
	}
}