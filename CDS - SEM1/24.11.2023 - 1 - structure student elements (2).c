//wap to accept student data in a structure and display the elements of the structure
//strucure elements : name,branch and registration number

#include <stdio.h>
struct student{
	char name[30],branch[20];
	long long int regdno;
};

void main(){
	struct student s1;
	printf("Enter student name :");
	scanf("%s",&s1.name);
	printf("Enter branch :");
	scanf("%s",&s1.branch);
	printf("Enter registration no :");
	scanf("%lld",&s1.regdno);
	printf("The student details are :");
	printf("\nName : %s \nBranch : %s \nRegistration Number : %lld",s1.name,s1.branch,s1.regdno);
	
}
