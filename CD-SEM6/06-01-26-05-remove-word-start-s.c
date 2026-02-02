// wap to remove all words starting s from a given file and display the updated content

#include <stdio.h>
#include <string.h>
#include <ctype.h>

void main() {
    FILE *file;
    char filename[100];
    char word[100];

    printf("Enter the path to the file: ");
    scanf("%s", filename);

    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Could not open file %s\n", filename);
        return;
    }

    printf("Updated content of the file:\n");

    while (fscanf(file, "%s", word) != EOF) {
        if (tolower(word[0]) != 's') {
            printf("%s ", word);
        }
    }

    printf("\n");
    fclose(file);
}
