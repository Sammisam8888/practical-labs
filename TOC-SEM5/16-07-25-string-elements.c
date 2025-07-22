#include <stdio.h>

int main(){
	char s[100];
	printf("Enter a string : ");
	scanf("%s",s);
	int alphabet=0,sp=0, digit=0,vowel=0,consonant=0;
//	int len = sizeof(a)/sizeof(a[0]);
	char *i=s;
	while (*i!='\0'){
		if ((*i<=90 && *i>=65) || (*i<=122 && *i>=97)){
			alphabet++;
			if (*i=='a' || *i=='e' || *i=='i' || *i=='o' ||*i=='u' || *i=='A'|| *i=='E' || *i=='I'||*i=='O'|| *i=='U'){
				vowel++;
			}
			else consonant++;
		}
		else if (*i>=48 && *i<=57){
			digit++;
		}
		else {
			sp++;
		}
		i++;
	}
	printf("In the given string %s\nThe no of alphabets are : %d, No of Vowels are : %d, No of Consonants are : %d",s,alphabet,vowel,consonant);
	printf("\nThe no of Digits are : %d\nThe number of Special characters are : %d",digit,sp);
}
//if (i=='=' && i=='!' || i=='@' || i=='#' || i=='$' || i=='%' || i=='&'|| i=='*' || i=='('||i==')'|| i=='-'||i=='_')