//find gcd among 2 numbers using recursion

#include <stdio.h>
int gcd(int n,int m){
	if (n==0)
		return m;
	else if (m==0)
		return n;
    if (m > n)
        return gcd(m % n, n);
    else
        return gcd(m, n % m);
}
void main(){
	int a,b;
	printf("Enter 2 numbers :");
	scanf("%d%d",&a,&b);
	int f = gcd(a,b);
	printf("The gcd of %d & %d is : %d",a,b,f);
}
