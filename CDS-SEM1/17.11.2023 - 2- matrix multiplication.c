//wap to take 2 matrices as input and show their product

#include <stdio.h>
void main()
{
	int m,n,x,y;
    int i,j, k;
    printf("Enter the number of rows of 1st matrix :");
    scanf("%d",&m);
    printf("Enter the number of columns of 1st matrix :");
    scanf("%d",&n);
    printf("Enter the number of rows of 2nd matrix :");
    scanf("%d",&x);
    printf("Enter the number of columns of 2nd matrix :");
    scanf("%d",&y);
    int a[m][n];
    int b[x][y];
    if (n!=x){
    	printf("Here number of columns of 1st matrix  is not equal to number of rows of 2nd matrix");
    	printf("\nHence multiplication of these 2 matrices is not possible");
	}
    else {
    	int p[m][y]={{0,0,0},{0,0,0},{0,0,0}};
    	printf("Enter the 1st matrix :%dx%d\n",m,n);
	    for(i=0;i<m;i++)
	    {
	    	printf("Enter details of %dth row :\n",i+1);
	        for(j=0;j<n;j++)
	        {
	        	printf("Enter the %dth element :",j+1);
	            scanf("%d", &a[i][j]);
	        }
	    }
    	printf("Enter the 2nd matrix :%dx%d\n",x,y);
	    for(i=0;i<x;i++)
	    {
	    	printf("Enter details of %dth row :\n",i+1);
	        for(j=0;j<y;j++)
	        {
	        	printf("Enter the %dth element :",j+1);
	            scanf("%d", &b[i][j]);
	        }
	    }
	    // for product matrix
	    for(i=0;i<m;i++){
	        for(j=0;j<y;j++){
	        for(k=0;k<x;k++){
	            p[i][j]+=a[i][k]*b[k][j]; //main logic for matrix multiplication
	    	}
	        }
	    }
	    printf("Matrix A = \n");
	    for(i=0;i<m;i++){
	    	for (j=0;j<n;j++){
	    		printf("%d ",a[i][j]);
			}
			printf("\n");
		}
	    printf("Matrix B = \n");
	    for(i=0;i<x;i++){
	    	for (j=0;j<y;j++){
	    		printf("%d ",b[i][j]);
			}
			printf("\n");
		}
	    printf("The product matrix P is :\n");
	    for(i=0;i<m;i++){
	    	for (j=0;j<y;j++){
	    		printf("%d ",p[i][j]);
			}
			printf("\n");
		}

	}	
}
	    
