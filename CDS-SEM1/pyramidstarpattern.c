#include<stdio.h>
//program to print the star pattern
int main(){
	int r;
	printf("enter the number of rows for pattern:");
	scanf("%d",&r);
	for(int i=1;i<=r;i++){
		for(int j=1;j<=(r-i);j++){
			printf(" ");
		}for(int j=1;j<=(2*i)-1;j++){
			if(j%2!=0){
				printf("*");
			}else{
				printf(" ");
			}
		}
		printf("\n");
	}
}