/*WAP to enter details of a student like name, branch, 
regd no, course and print them */

#include <stdio.h>
int main(){
	char name[30],course[10],branch[5];
	unsigned long int regno;
	printf("Enter student details \nEnter your name :");
	gets(name);
	printf("Enter your course :");
	gets(course);
	printf("Enter your branch :");
	gets(branch);
	printf("Enter your registration number :");
	scanf("%ld",&regno);
	printf("\nThe student details are : \nName : %s\nCourse : %s\nBranch : %s \nRegistration No. : %u",name,course,branch,regno);
	return 0;
}
