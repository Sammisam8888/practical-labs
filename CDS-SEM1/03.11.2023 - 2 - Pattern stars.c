/*
WAP to print the pattern :
		*
	*	*	*
*	*	*	*	*	...& so on as per user demand	*/

#include<stdio.h>
void main(){
	int r,i,j;
	printf("enter the number of rows for pattern:");
	scanf("%d",&r);
	for(i=1;i<=r;i++){
		for(j=1;j<=(r-i);j++){
			printf(" ");}
		for(j=1;j<=(2*i)-1;j++){
			if(j%2!=0)
				printf("*");
			else
				printf(" ");
		}
		printf("\n");
	}
}
