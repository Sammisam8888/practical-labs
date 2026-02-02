// wap in c to count alphabet and digit special character in a input string

#include <stdio.h>

void main(){
    char str[100];
    printf("Enter a string: ");
    scanf("%[^\n]s", str);
    int alpha=0, digit=0, special=0;
    for(int i=0; str[i]!='\0'; i++){
        if((str[i]>='a' && str[i]<='z') || (str[i]>='A' && str[i]<='Z')){
            alpha++;
        }
        else if(str[i]>='0' && str[i]<='9'){
            digit++;
        }
        else{
            special++;
        }
    }
    printf("Alphabets count : %d\n", alpha);
    printf("Digits count : %d\n", digit);
    printf("Special characters count : %d\n", special);
}