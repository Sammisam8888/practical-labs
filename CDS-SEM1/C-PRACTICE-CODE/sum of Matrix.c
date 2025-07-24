#include<stdio.h>
int main(){
	int r,c;
	printf("Enter no of rows :");
	scanf("%d",&r);
	printf("Enter no of columns :");
	scanf("%d",&c);
	int a[r][c],b[r][c],s[r][c];
	printf("Enter 1st matrix : \n");
	for (int i=0;i<r;i++){
		for (int j=0;j<c;j++){
			scanf("%d",&a[i][j]);
		}
		printf("\n");
	}
	printf("\nEnter 2nd matrix : \n");
	for (int i=0;i<r;i++){
		for (int j=0;j<c;j++){
			scanf("%d",&b[i][j]);
		}
		printf("\n");
	}
	printf("Sum of the matrix is :\n");
	for (int i=0;i<r;i++){
		for (int j=0;j<c;j++){
			s[i][j]=a[i][j]+b[i][j];
			printf("%d ",s[i][j]);
		}
		printf("\n");
	}
	return 0;
}