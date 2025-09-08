#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main() {
    pid_t pid = fork();

    if (pid < 0) {
        perror("fork failed");
        return 1;
    } else if (pid == 0) {
        // Child process
        printf("Child -> My PID is %d, My Parent's PID is %d\n", getpid(), getppid());
    } else {
        // Parent process
        printf("Parent -> My PID is %d, My Parent's PID is %d\n", getpid(), getppid());
    }

    return 0;
}