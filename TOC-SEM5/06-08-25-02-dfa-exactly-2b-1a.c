//atleast 1a & exactly 2b

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool q1(char s[],int i);
bool q2(char s[],int i);
bool q3(char s[],int i);
bool q4(char s[],int i);
bool q5(char s[],int i);

bool q0(char s[],int i){
	if (s[i]=='\0') return 0; 
	else if (s[i]=='a') return q4(s,++i);
	else return q1(s,++i);
}

bool q1(char s[],int i){
	if (s[i]=='\0') return 0; 
	else if (s[i]=='a') return q5(s,++i); //reject state
	else return q2(s,++i);
}

bool q2(char s[],int i){
	if (s[i]=='\0') return 0; 
	else if (s[i]=='a') return q3(s,++i);
	else return 0;
}

bool q3(char s[],int i){
	if (s[i]=='\0') return 1; //satisfied   
	else if (s[i]=='b') return 0; //reject state
	else return q3(s,++i);
}

bool q4(char s[],int i){
    if (s[i]=='\0') return 0; 
    else if (s[i]=='b') return q5(s,++i);
    else return q4(s,++i);
}
 
bool q5(char s[],int i){
    if (s[i]=='\0') return 0; 
    else if (s[i]=='b') return q3(s,++i);
    else return q5(s,++i);
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
	
	printf("The given string %s %s satisfy the condition of atleast 1a & exactly 2b\n",s,(q0(s,0)?"does":"doesn't"));
	return 0;
}