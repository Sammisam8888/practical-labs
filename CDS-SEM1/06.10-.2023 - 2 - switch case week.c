/* WAP to enter a number from 1 to 7 and display the corresponding 
day of the week using switch case statement */

#include <stdio.h>
void main(){
	int i;
	printf("Enter a number between 1 and 7 :");
	scanf("%d",&i);
	printf("The corresponding day of the week is :");
	switch(i){
		case 1:
			printf("Sunday"); break;
		case 2:
			printf("Monday"); break;
		case 3:
			printf("Tuesday"); break;
		case 4:
			printf("Wednesday"); break;
		case 5:
			printf("Thursday"); break;
		case 6:
			printf("Friday"); break;
		case 7:
			printf("Saturday"); break;
		default :
			printf("The value entered is greater than 7");	
	}
	
}
