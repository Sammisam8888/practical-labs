#include <stdio.h>
#include <stdlib.h>

int main(){
	char s[100],subs[100];
	printf("Enter a string : ");
	scanf("%s",s);
	printf("Enter a substring : ");
	scanf("%s",subs);
	
	int substring = 0;
	char *i=s;
	while (*i != '\0'){
		char *p = i;
		char *j=subs;
		while (*j != '\0' && *p!='\0'){
			if (*p==*j){
				j++;
				p++;
			}
			else break;
		}
		if (*j=='\0') substring++;
		i++; 
		
	}

	printf("The number of times %s repeats in %s is : %d",subs,s,substring);
	return 0;
}