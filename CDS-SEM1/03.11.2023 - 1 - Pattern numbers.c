/*WAP to print the pattern :
1
1 2
1 2 3
1 2 3 4 ... & so on as per the user demand */
#include <stdio.h>
void main(){
	int i,j,n;
	printf("Enter number of rows :");
	scanf("%d",&n);
	for (i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			if (j<=i)
				printf("%d ",i);
			else 
				printf("  ");			
		}
		printf("\n");
	}
}