//implement dining philosopher problem using monitor solution in C language

#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

#define N 5               
#define THINKING 0
#define HUNGRY 1
#define EATING 2
#define ROUNDS 2         

pthread_mutex_t mutex;
pthread_cond_t cond[N];
int state[N];

void test(int i) {
    if (state[i] == HUNGRY &&
        state[(i + N - 1) % N] != EATING &&
        state[(i + 1) % N] != EATING) {
        state[i] = EATING;
        pthread_cond_signal(&cond[i]);
    }
}

void pickup(int i) {
    pthread_mutex_lock(&mutex);
    state[i] = HUNGRY;
    printf("Philosopher %d is Hungry\n", i + 1);
    test(i);
    while (state[i] != EATING)
        pthread_cond_wait(&cond[i], &mutex);
    pthread_mutex_unlock(&mutex);
}

void putdown(int i) {
    pthread_mutex_lock(&mutex);
    state[i] = THINKING;
    printf("Philosopher %d puts down forks and starts Thinking\n", i + 1);
    test((i + N - 1) % N);
    test((i + 1) % N);
    pthread_mutex_unlock(&mutex);
}

void* philosopher(void* num) {
    int i = *(int*)num;
    for (int round = 0; round < ROUNDS; round++) {
        printf("Philosopher %d is Thinking\n", i + 1);
        sleep(1);
        pickup(i);
        printf("Philosopher %d is Eating (Round %d)\n", i + 1, round + 1);
        sleep(2);
        putdown(i);
    }
    printf("Philosopher %d has finished dining.\n", i + 1);
    return NULL;
}

int main() {
    pthread_t tid[N];
    int phil[N];

    pthread_mutex_init(&mutex, NULL);
    for (int i = 0; i < N; i++)
        pthread_cond_init(&cond[i], NULL);

    for (int i = 0; i < N; i++) {
        phil[i] = i;
        pthread_create(&tid[i], NULL, philosopher, &phil[i]);
    }

    for (int i = 0; i < N; i++)
        pthread_join(tid[i], NULL);

    pthread_mutex_destroy(&mutex);
    for (int i = 0; i < N; i++)
        pthread_cond_destroy(&cond[i]);

    printf("\nAll philosophers have finished dining. Exiting program.\n");
    return 0;
}
