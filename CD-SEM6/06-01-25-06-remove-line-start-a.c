// wap to remove a line which starts with 'a' from a given file and display the updated content
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void main() {
    FILE *file, *tempFile;
    char filename[100], tempFilename[] = "temp.txt";
    char line[256];

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

    while (fgets(line, sizeof(line), file)) {
        if (tolower(line[0]) != 'a') {
            fputs(line, tempFile);
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
    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
    }

    fclose(file);
}