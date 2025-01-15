//wap to swap 2 numbers using call by value and call by reference

#include <stdio.h>
int a,b;
void swapint(int c,int d){
	int temp=c;
	c=d;d=temp;
	printf("\nAfter swapping (call by value) : a=%d & b=%d",c,d);
}
void swappointer(int *p,int *q){
	int temp;
	temp=*p; *p=*q; *q=temp;
}
void main(){
	printf("Enter 2 numbers :");
	scanf("%d%d",&a,&b);
	printf("Before swapping : a=%d & b=%d",a,b);
	swapint(a,b);
	swappointer(&a,&b);
	//a=5
	printf("\nAfter swapping (call by reference) : a=%d & b=%d", a,b);
}
