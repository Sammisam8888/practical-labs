// wap to remove all words starting s from a given file and display the updated content

#include <stdio.h>
#include <string.h> 
#include <stdlib.h>
#include <ctype.h>

void main() {
    FILE *file, *tempFile;
    char filename[100], tempFilename[] = "temp.txt";
    char word[100];

    printf("Enter the path to the file: ");
    scanf("%s", filename);

    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Could not open file %s\n", filename);
        return;
    }

    tempFile = fopen(tempFilename, "w");
    if (tempFile == NULL) {
        printf("Could not create temporary file\n");
        fclose(file);
        return;
    }

    while (fscanf(file, "%s", word) != EOF) {
        if (tolower(word[0]) != 's') {
            fprintf(tempFile, "%s ", word);
        }
    }

    fclose(file);
    fclose(tempFile);

    // Replace original file with updated content
    remove(filename);
    rename(tempFilename, filename);

    // Display updated content
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Could not open file %s\n", filename);
        return;
    }

    printf("Updated content of the file:\n");
    while (fscanf(file, "%s", word) != EOF) {
        printf("%s ", word);
    }
    printf("\n");

    fclose(file);
}