//Wap to find maximum and minimum of the elements present in an array
#include <stdio.h>
void main(){
	int n,i;
	printf("Enter number of elements in array :");
	scanf("%d",&n);
	int a[n];
	printf("Enter the elements of the array :\n");
	for (i=0;i<n;i++){
		printf("%d th element : ",i+1);
		scanf("%d",&a[i]);
	}
	int min=a[0],max=a[0];
	for (i=0;i<n;i++){
		if (a[i]<min)
			min=a[i];
		if (a[i]>max)
			max=a[i];
	}
	printf("The minimum value in array is : %d",min);
	printf("\nThe maximum value in array is : %d",max);
	
}