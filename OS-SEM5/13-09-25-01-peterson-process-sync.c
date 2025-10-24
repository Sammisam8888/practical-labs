// Peterson's solution for process synchronization in C using pthreads

#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdbool.h>

volatile bool flag[2];
volatile int turn;

void *process(void *arg) {
    int id = *(int *)arg;
    int other = 1 - id;

    for (int i = 0; i < 3; i++) {
        flag[id] = true;
        turn = other;

        while (flag[other] && turn == other)
            ;

        printf("Process %d is in critical section (iteration %d)\n", id, i + 1);
        sleep(1);

        flag[id] = false;

        printf("Process %d is in remainder section\n", id);
        sleep(1);
    }

    return NULL;
}

int main(void) {
    pthread_t t1, t2;
    int ids[2] = {0, 1};

    printf("Peterson's Solution for Process Synchronization (C, pthreads)\n");

    flag[0] = false;
    flag[1] = false;
    turn = 0;

    pthread_create(&t1, NULL, process, &ids[0]);
    pthread_create(&t2, NULL, process, &ids[1]);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("\nBoth processes finished execution safely.\n");
    return 0;
}
