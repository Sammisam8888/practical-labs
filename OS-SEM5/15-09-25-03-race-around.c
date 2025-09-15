//Wap to demonstrate the race around condition using fork or pthread..

#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

int counter = 0; // shared variable

void* increment(void* arg) {
    for (int i = 0; i < 100000; i++) {
        // Race condition: no synchronization
        counter = counter + 1;
    }
    return NULL;
}

int main() {
    pthread_t t1, t2;

    pthread_create(&t1, NULL, increment, NULL);
    pthread_create(&t2, NULL, increment, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("Final counter value: %d\n", counter);
    // Expected: 200000, but due to race condition, it's usually less
    return 0;
}
