//wap to count no of vowel and consonant in a string
#include <stdio.h>
#include <string.h>
void main(){
	char s[50];
	printf("Enter a string :");
	gets(s);
	int i=0,v=0,c=0;
	while (s[i]!='\0'){
		if (s[i]=='a'||s[i]=='e'||s[i]=='i'||s[i]=='i'||s[i]=='o'||s[i]=='u')
			v++;
		else if (s[i]=='A'||s[i]=='E'||s[i]=='I'||s[i]=='O'||s[i]=='U')
			v++;
		else if (s[i]<91 && s[i]>=65 || s[i]<123&&s[i]>=96){
			c++;
		}
		i++;
	}
printf("The number of vowels in %s is : %d",s,v);
printf("\nThe number of consonants is : %d",c);
}

