//WAP to demonstrate logical operators : && and, || or

#include <stdio.h>
void main(){
	int x,y;
	printf("Enter 2 numbers :");
	scanf("%d%d",&x,&y);
	printf("Logical AND operator :\n%d && %d\n",x,y);
	if (x&&y){
		printf("AND condition True"); }
	else {
		printf("AND condition False");}
	printf("\nLogical OR operator :\n%d && %d\n",x,y);
	if (x||y){
		printf("OR condition True");}
	else {
		printf("OR condition False");}
	printf("\nLogical NOT operator\n");
	int a=0,b=1;
	printf("NOT of 0 is : %d",!a);
	printf("\nNOT of 1 is : %d",!b);
}
	
	
