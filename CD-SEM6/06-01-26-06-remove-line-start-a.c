// wap to remove a line which starts with 'a' from a given file and display the updated content
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void main() {
    FILE *file;
    char filename[100];
    char line[256];

    printf("Enter the path to the file: ");
    scanf("%s", filename);

    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Could not open file %s\n", filename);
        return;
    }

    printf("Updated content of the file:\n");

    while (fgets(line, sizeof(line), file)) {
        if (tolower(line[0]) != 'a') {
            printf("%s", line);
        }
    }

    fclose(file);
}
