//WAP to find the gcd and lcm of given 2 numbers using function 
#include <stdio.h>
void gcd(int n,int m){
	int a[n],b[m],j=0;
	for (int i=0;i<n;i++){
		if (n%i!=0){
			a[j]=i;j++;			
		}
	}
	j=0;
	for (i=0;i<m;i++){
		if (m%i!=0){
			b[j]=i;j++;
		}
	}
	for (i=0;i<j;i++){
		for (int k=0;k<i;k++){	
	}