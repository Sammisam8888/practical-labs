//WAP to  demonstrate interprocess communication using shared memory between a parent and a child process

#include <stdio.h>
#include <unistd.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <string.h>
#include <stdlib.h>

#define SHM_SIZE 1024

void child(int shmid) {
    // Attach to shared memory
    char *shmaddr = (char *)shmat(shmid, NULL, 0);
    if (shmaddr == (char *)-1) {
        perror("shmat in child");
        exit(1);
    }

    printf("Child: Reading from shared memory...\n");
    printf("Child: Data from parent: %s\n", shmaddr);

    // Write response
    strcpy(shmaddr, "Hello from child!");

    // Detach
    shmdt(shmaddr);
}

void parent(int shmid, pid_t cpid) {
    // Attach to shared memory
    char *shmaddr = (char *)shmat(shmid, NULL, 0);
    if (shmaddr == (char *)-1) {
        perror("shmat in parent");
        exit(1);
    }

    // Write message
    strcpy(shmaddr, "Hello from parent!");

    // Wait for child to finish
    wait(NULL);

    // Read child's response
    printf("Parent: Data from child: %s\n", shmaddr);

    // Detach and remove shared memory
    shmdt(shmaddr);
    shmctl(shmid, IPC_RMID, NULL);
}

int main() {
    int shmid;
    key_t key = IPC_PRIVATE;

    // Create shared memory segment
    shmid = shmget(key, SHM_SIZE, IPC_CREAT | 0666);
    if (shmid < 0) {
        perror("shmget");
        return 1;
    }

    pid_t pid = fork();
    if (pid < 0) {
        perror("fork");
        return 1;
    } else if (pid == 0) {
        // Child process
        child(shmid);
        exit(0);
    } else {
        // Parent process
        parent(shmid, pid);
    }

    return 0;
}