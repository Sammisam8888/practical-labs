#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid = fork();

    if (pid == 0) {
        // Child process
        printf("Child (PID: %d) is exiting now.\n", getpid());
        exit(0); // Child terminates immediately
    } else {
        // Parent process
        printf("Parent is sleeping for 20 seconds, not waiting for child.\n");
        sleep(20); // Parent does not reap the child
        printf("Parent is done sleeping.\n");
    }

    return 0;
}