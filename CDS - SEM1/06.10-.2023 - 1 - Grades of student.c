/*WAP in C to enter the marks of student in 4 subjects, then calculate the total aggregate percentage 
and display grade obtained by the student : O - above 90%, A+ - Above 80%, A - Above 70%, B+ - Above 60%, 
B - Above 50%, C - Above 40%, F (fail) - Below 40% */
#include <stdio.h>
void main(){
	int p,c,m,cs,ful;
	printf("Enter full marks in all subjects combined :");
	scanf("%d",&ful);
	printf("Enter marks obtained by student in physics :");
	scanf("%d",&p);
	printf("Enter marks obtained in chemistry :");
	scanf("%d",&c);
	printf("Enter marks obtained in maths : ");
	scanf("%d",&m);
	printf("Enter marks obtained in computer science :");
	scanf("%d",&cs);
	float per=(float)((p+c+m+cs)*100/ful);
	printf("The students grade is :");
	if (per>=90)
		printf("O - Outstanding!");
	else if(per>=80)
		printf("A+");
	else if (per>=70)
		printf("A");
	else if (per>=60)
		printf("B+");
	else if (per>=50)
		printf("B");
	else if (per>=40)
		printf("C");
	else 
		printf("F - Failed");
	
}
	
