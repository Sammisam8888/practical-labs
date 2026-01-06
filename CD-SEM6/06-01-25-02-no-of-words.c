// wap to count number of words in a file (txt file) 

#include <stdio.h>
#include <ctype.h>

void main(){
    FILE *file;
    char filename[100], ch;
    int words = 0, inWord = 0;

    printf("Enter the path to the file : ");
    scanf("%s", filename);

    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Could not open file %s\n", filename);
        return;
    }

    while ((ch = fgetc(file)) != EOF) {
        if (isspace(ch)) {
            inWord = 0;
        } else {
            if (inWord == 0) {
                words++;
                inWord = 1;
            }
        }
    }

    fclose(file);
    printf("Number of words in the file: %d\n", words);
}