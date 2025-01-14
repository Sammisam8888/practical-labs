#include<stdio.h>
int swap(){
	int temp,a,b;
	printf("enter two numbers to be swapped:");
	scanf("%d%d",&a,&b);
	temp=a;
	a=b;
	b=temp;
	printf("the value of a=%d,",a);
	printf("\nthe value of b=%d",b);
}
int main(){
	swap();
	return 0;
}