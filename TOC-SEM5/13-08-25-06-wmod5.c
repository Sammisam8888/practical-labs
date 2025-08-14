// L= {w: |w| mod 5 ≠ 0}.

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool q1(char s[],int i);
bool q2(char s[],int i);
bool q3(char s[],int i);
bool q4(char s[],int i);

bool q0(char s[],int i){
	if (s[i]=='\0') return 0; 
	else return q1(s,++i);
}

bool q1(char s[],int i){
	if (s[i]=='\0') return 1; 
	else return q2(s,++i);
}

bool q2(char s[],int i){
	if (s[i]=='\0') return 1; 
	else return q3(s,++i);
}

bool q3(char s[],int i){
	if (s[i]=='\0') return 1; 
	else return q4(s,++i);
}

bool q4(char s[],int i){
	if (s[i]=='\0') return 1; 
	else return q0(s,++i);
}

int main(){
	printf("Enter a string containing only (a or b) : ");
	char s[100];
	scanf("%s",s);
	int i=0;

	while (s[i]!='\0'){
		if (!(s[i]=='a' || s[i]=='b')){
			printf("The provided input is not a valid combination of a & b");
			exit(0);
		}
		i++;
	}

	printf("The given string %s %s satisfy the condition of |w| mod 5 != 0 \n",s,(q0(s,0)?"does":"doesn't"));
	return 0;
}