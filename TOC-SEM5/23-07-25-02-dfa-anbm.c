#include <stdio.h>
#include <stdbool.h>


bool q1(int n,int m);
bool q2(int n,int m);
bool q3(int n,int m);

bool q0(int n,int m){
	if (n!=0) return q1(--n,m);
	else if (m!=0) return q3(n,--m);
	else return 0;
}

bool q1(int n,int m){
	if (n!=0) return q0(--n,m);
	else if (m!=0) return q2(n,--m);
	else return 0;
}

bool q2(int n,int m){
	if (n!=0) return q3(--n,m);
	else if (m!=0) return q2(n,--m);
	else return 0;
}

bool q3(int n,int m){
	if (n!=0) return q2(--n,m);
	else if (m!=0) return q3(n,--m);
	else return 1;
}

int main(){
	int n,m;
	printf("Enter the power of a (a^n) : ");
	scanf("%d",&n);
	printf("Enter the power of b (b^m) (m>=1) : ");
	scanf("%d",&m);
	
	printf("The given conditions of : n mod 2=0 & m>=1 over a^%d*b^%d is %s\n",n,m,(q0(n,m)?"satisfied":"not satisfied"));
	
	
	return 0;
}