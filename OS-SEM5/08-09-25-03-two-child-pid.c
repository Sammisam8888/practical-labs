#include <stdio.h>
#include <stdlib.h>   // For exit()
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h> // For wait()

int main() {
    pid_t child1, child2;

    // Create the first child
    child1 = fork();

    if (child1 < 0) {
        perror("First fork failed");
        return 1;
    }

    if (child1 == 0) {
        // First child's code
        printf("I am the first child, my PID is %d.\n", getpid());
        exit(0); // Child exits
    } else {
        // Parent's code continues
        // Create the second child
        child2 = fork();

        if (child2 < 0) {
            perror("Second fork failed");
            return 1;
        }

        if (child2 == 0) {
            // Second child's code
            printf("I am the second child, my PID is %d.\n", getpid());
            exit(0); // Child exits
        } else {
            // Parent waits for both children to finish
            wait(NULL);
            wait(NULL);
            printf("I am the parent, and both my children have finished.\n");
        }
    }

    return 0;
}