//check if the inputted string is pallindrome or not

#include <stdio.h>
#include <string.h>
void main(){
	char s[50];
	printf("Enter a string :");
	scanf("%s",&s);
	int i,m=0;
	int n= strlen(s);
	for (i=0;i<n;i++){
		if (s[i]==s[n-i-1]){
			m=1; continue;
		}
		else 
			m=0;
			break;
	}
	if (m==1)
		printf("The string %s is a pallindrome",s);
	else 
		printf("The string %s is not a pallindrome",s);
}
