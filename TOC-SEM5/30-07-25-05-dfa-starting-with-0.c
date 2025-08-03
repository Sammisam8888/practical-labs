#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool q0(char s[],int i){
	if (s[i]=='\0') return 0; //reject state 
	else if (s[i]=='1') return 0; //reject state 
	else if (s[i]=='0') return 1; //satisfied - start with 0
	else{
		printf("The provided input is not a valid binary number");
		exit(0);
	}
}

int main(){
	printf("Enter a binary string containing only (0 or 1) : ");
	char s[100];
	scanf("%s",s);
	int i=0;
	
	printf("The given binary number %s %s start with 0",s,(q0(s,0)?"does":"doesn't"));
	return 0;
}