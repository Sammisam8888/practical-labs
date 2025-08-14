//L= {ab^5wb^2: w ∈ {a,b}*}

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool q1(char s[],int i);
bool q2(char s[],int i);
bool q3(char s[],int i);
bool q4(char s[],int i);
bool q5(char s[],int i);
bool q6(char s[],int i);
bool q7(char s[],int i);

bool q0(char s[],int i){
	if (s[i]=='\0') return 0; 
	else if (s[i]=='a') return q1(s,++i);
	else return 0;
}

bool q1(char s[],int i){
	if (s[i]=='\0') return 0; 
	else if (s[i]=='a') return 0; 
	else return q2(s,++i);
}

bool q2(char s[],int i){
	if (s[i]=='\0') return 0; 
	else if (s[i]=='b') return q3(s,++i);
	else return 0;
}

bool q3(char s[],int i){
	if (s[i]=='\0') return 0; 
	else if (s[i]=='a') return 0; //reject state
	else return q4(s,++i);
}

bool q4(char s[],int i){
    if (s[i]=='\0') return 0; 
    else if (s[i]=='b') return q5(s,++i);
    else return 0;
}
 
bool q5(char s[],int i){
    if (s[i]=='\0') return 0; 
    else if (s[i]=='b') return q6(s,++i);
    else return 0;
}

bool q6(char s[],int i){
    if (s[i+2]!='\0') return q6(s,++i); //continue until last 2 characters are encountered
    else if (s[i]=='\0') return 0; 
    else if (s[i]=='b') return q7(s,++i);
    else return 0;
}

bool q7(char s[],int i){
    if (s[i]=='\0') return 0; 
    else if (s[i]=='b') return 1; //satisified
    else return 0;
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
	
	printf("The given string %s %s satisfy the condition of ab^5wb^2: w ∈ {a,b}*\n",s,(q0(s,0)?"does":"doesn't"));
	return 0;
}