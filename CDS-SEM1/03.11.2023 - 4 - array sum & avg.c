//WAP to create an array and find sum & average of element present in array

#include <stdio.h>
void main(){
	int n,i,s=0;
	printf("Enter number of elements in array :");
	scanf("%d",&n);
	int a[n];
	printf("Enter the elements of the array :\n");
	for (i=0;i<n;i++){
		printf("%d th element : ",i+1);
		scanf("%d",&a[i]);
	}
	for (i=0;i<n;){
		s+=a[i++];
	}
	printf("The sum of all elements in the array is : %d",s);
	printf("\nThe average of all elements in array is : %f",(float)s/n);
}