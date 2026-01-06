// wap to check if the given input is a valid identifier

#include <stdio.h>
#include <string.h>
#include<stdlib.h>


void main(){
    char id[100];
    printf("Enter the identifier :");
    scanf("%s",id);

    if (strlen(id) == 0){
        printf("Invalid identifier, it cannot be empty");
        exit(0);
    }

    char keywords[32][10] = {"auto","break","case","char","const","continue","default","do","double","else","enum","extern","float","for","goto","if","int","long","register","return","short","signed","sizeof","static","struct","switch","typedef","union","unsigned","void","volatile","while"};

    for (int k=0;k<32;k++){
        if (strcmp(id,keywords[k])==0){
            printf("Invalid identifier, it is a keyword\n");
            exit(0);
        }
    }

    for (int i=0;id[i]!='\0';i++){
        if (i==0){
            if ((id[i]<='z' && id[i]>='a')||(id[i]<='Z' && id[i]>='A')){
                continue;
            }
            else {
                printf("Invalid identifier, first character needs to be an alphabet\n");
                exit(0);
            }
        }
        else{
            if ((id[i]<='z' && id[i]>='a')||(id[i]<='Z' && id[i]>='A')||(id[i]<='9' && id[i]>='0')||id[i]=='_'){
                continue;
            }
            else{
                printf("Invalid identifier, it cannot contain anything other than alphabet, numbers or underscore (_)\n");
                exit(0);
            }
        }
    }
    printf("Identifier is valid\n");
}