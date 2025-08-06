//atmost 2a and more than 2b

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool q01(char s[],int i);
bool q02(char s[],int i);
bool q10(char s[],int i);
bool q11(char s[],int i);
bool q12(char s[],int i);
bool q20(char s[],int i);
bool q21(char s[],int i);
bool q22(char s[],int i);

bool q00(char s[],int i){
	if (s[i]=='\0') return 1; 
	else if (s[i]=='a') return q10(s,++i);
	else return q01(s,++i);
}

bool q01(char s[],int i){
	if (s[i]=='\0') return 0; 
	else if (s[i]=='a') return q11(s,++i); //reject state
	else return q02(s,++i);
}

bool q02(char s[],int i){
	if (s[i]=='\0') return 0; 
	else if (s[i]=='a') return q12(s,++i);
	else return q00(s,++i);
}

bool q10(char s[],int i){
	if (s[i]=='\0') return 1; //satisfied   
	else if (s[i]=='a') return q20(s,++i) ; //reject state
	else return q11(s,++i);
}

bool q11(char s[],int i){
    if (s[i]=='\0') return 1; 
    else if (s[i]=='a') return q21(s,++i);
    else return q12(s,++i);
}

bool q12(char s[],int i){
    if (s[i]=='\0') return 0; 
    else if (s[i]=='a') return q22(s,++i);
    else return q10(s,++i);
}


bool q20(char s[],int i){
    if (s[i]=='\0') return 0; 
    else if (s[i]=='a') return q00(s,++i);
    else return q21(s,++i);
}


bool q21(char s[],int i){
    if (s[i]=='\0') return 0; 
    else if (s[i]=='a') return q02(s,++i);
    else return q22(s,++i);
}


bool q22(char s[],int i){
    if (s[i]=='\0') return 1; 
    else if (s[i]=='a') return q02(s,++i);
    else return q20(s,++i);
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
	
	printf("The given string %s %s satisfy the condition of a mod 3 = b mod 3\n",s,(q00(s,0)?"does":"doesn't"));
	return 0;
}