//find factorial  of a number using recursion

#include <stdio.h>

int fact(int n){
	if ((n==1)||(n==0))
		return 1;
	else {
		return n*fact(n-1); 
	}
}
int main(){
	int n;
	printf("Enter a number :");
	scanf("%d",&n);
	int f=fact(n);
	printf("The factorial of the number is : %d",f);
	return 0;
}

