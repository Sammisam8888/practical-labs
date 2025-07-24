//WAP to convert decimal to binary

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
void decbin(int b){
    int d=0;
    while(b>0){
        d=d*10+b%2;
        b/=2;
    }
    printf ("The binary value is %d",rev(d));
}
void main()
{
    int d;
    printf("Enter a decimal number :");
    scanf("%d ",&d);
    decbin(d);
}