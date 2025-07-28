#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr = (int *)malloc(5 * sizeof(int));

    if (ptr == NULL) {
        printf("Memory cannot be allocated\n");
        return 1; 
    }

    for (int i = 0; i < 5; i++) {
        ptr[i] = i;
    }

    printf("Values stored in allocated memory are:\n");
    for (int i = 0; i < 5; i++) {
        printf("%d ", ptr[i]);
    }

    // Reallocate memory for 10 integers
    int *newPtr = (int *)realloc(ptr, 10 * sizeof(int));

    if (newPtr == NULL) {
        printf("Memory reallocation failed\n");
        free(ptr); 
        return 1;
    }

    // Update the pointer to the newly allocated memory
    ptr = newPtr;

    // Assign values to the newly allocated memory
    for (int i = 5; i < 10; i++) {
        ptr[i] = i;
    }

    printf("\nValues stored in reallocated memory are:\n");
    for (int i = 0; i < 10; i++) {
        printf("%d ", ptr[i]);
    }
    free(ptr);
    return 0;
}