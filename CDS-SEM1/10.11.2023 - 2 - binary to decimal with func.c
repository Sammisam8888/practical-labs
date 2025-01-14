#include <stdio.h>
int rev(int b){
	int b1=b%10;
	b=b/10;
	while(b!=0){
		b1=b1*10+b%10;
		b/=10;	
	}
	return b1;
}
int bindec(int b){
	int i,d;
	b=rev(b); d=b%10; b/=10;
	while (b!=0){
		d=(d*2)+b%10;
		b/=10;
	}
	return d;
}

void main(){
	int b,d;
	printf("Enter a binary number : ");
	scanf("%d",&b);
	d=bindec(b);
	printf("The decimal value is : %d",d);
	
}
