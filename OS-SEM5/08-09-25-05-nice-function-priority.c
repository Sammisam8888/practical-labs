#include <stdio.h>
#include <unistd.h>

int main() {
    // Get the current nice value by calling nice with an increment of 0
    int current_nice = nice(0);
    printf("Current nice value is: %d (Default Priority)\n", current_nice);

    // Increase the nice value by 5, which lowers the process priority
    nice(5);

    // Check the new nice value
    int new_nice = nice(0);
    printf("New nice value is: %d (Lower Priority)\n", new_nice);

    return 0;
}