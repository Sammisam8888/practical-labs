#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool q1(char s[],int i);
bool q2(char s[],int i);

bool q0(char s[],int i){
	if (s[i]=='\0') return 0;
	else if (s[i]=='1') return q0(s,++i);
	else return q1(s,++i);
}

bool q1(char s[],int i){
	if (s[i]=='\0') return 0;
	else if (s[i]=='0') return q1(s,++i);
	else return q2(s,++i);
}

bool q2(char s[],int i){
	if (s[i]=='\0') return 1;
	else if (s[i]=='1') return q0(s,++i);
	else return q1(s,++i);
}

int main(){
	printf("Enter a binary string containing only (0 or 1) : ");
	char s[100];
	scanf("%s",s);
	int i=0;
	while (s[i]!='\0'){
		if (!(s[i]=='0' || s[i]=='1')){
			printf("The provided input is not a valid binary number");
			exit(0);
		}
		i++;
	}
	printf("The given binary number %s %s end with 01\n",s,(q0(s,0)?"does":"doesn't"));
	return 0;
}