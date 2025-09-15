#include <stdio.h>    
#include <unistd.h>   
#include <sys/types.h>

int main() {
    pid_t pid = fork(); // Create a new process

    if (pid < 0) {
        // Error handling
        perror("fork failed");
        return 1;
    } else if (pid == 0) {
        // This block is executed by the child process
        printf("Hello from the child process! \n");
    } else {
        // This block is executed by the parent process
        printf("Hello from the parent process! \n");
    }

    return 0;
}