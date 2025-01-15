//WAP to find the gcd and lcm of given 2 numbers using function 

#include <stdio.h>
int gcd(int m,int n){
	int i;
	if (m>n){
		int temp=m;m=n;n=temp;
	}
	int hcf=1;
	for (i=1;i<m;i++){
		if (m%i==0 && n%i==0){
			if(hcf<i)
				hcf=i;
		}
	}
return hcf;
}
int lcm(int a,int b){
     return ((a*b)/gcd(a,b));
}
void main(){
	int a,b;
	printf("Enter 2 numbers :");
	scanf("%d%d",&a,&b);
	printf("The GCD of %d & %d is : %d",a,b,gcd(a,b));
	printf("\nThe LCM of %d & %d is : %d",a,b,lcm(a,b));
}
