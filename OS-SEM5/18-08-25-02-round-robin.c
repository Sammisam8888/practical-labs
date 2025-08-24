#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void sortbyarrival(int n, int* at, int* bt, int* pid) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (at[j] < at[i]) {
                swap(&at[i], &at[j]);
                swap(&bt[i], &bt[j]);
                swap(&pid[i], &pid[j]);
            }
        }
    }
}

void roundrobin(int n, int *pid, int* at, int* bt, double* rr) {
    int tq;
    printf("Enter Time Quantum: ");
    scanf("%d", &tq);

    int ct[n], wt[n], tat[n], btr[n];
    for (int i = 0; i < n; i++) btr[i] = bt[i];

    int time = 0, completed = 0, wtsum = 0, tatsum = 0;

    // Queue for processes
    int q[100], front = 0, rear = 0;
    int visited[n];
    for (int i = 0; i < n; i++) visited[i] = 0;

    printf("\nGantt Chart:\n");
    // Start by pushing first arrived process
    q[rear++] = 0;
    visited[0] = 1;

    while (front < rear) {
        int i = q[front++];
        if (time < at[i]) time = at[i]; // CPU idle till arrival

        printf("| %d P%d ", time, pid[i]);

        if (btr[i] <= tq) {
            time += btr[i];
            btr[i] = 0;
            completed++;
            ct[i] = time;
            tat[i] = ct[i] - at[i];
            wt[i] = tat[i] - bt[i];
            wtsum += wt[i];
            tatsum += tat[i];
        } 
        else {
            time += tq;
            btr[i] -= tq;
        }

        printf("%d", time);

        // Enqueue processes that have arrived till current time
        for (int j = 0; j < n; j++) {
            if (at[j] <= time && btr[j] > 0 && !visited[j]) {
                q[rear++] = j;
                visited[j] = 1;
            }
        }

        // If current process still not finished, push it back
        if (btr[i] > 0) q[rear++] = i;
    }

    printf("|\n\n");

    // Final Table
    printf("Task    Arrival Time   Burst Time     Waiting Time   Completion Time   Turnaround Time \n");
    for (int i = 0; i < n; i++) {
        printf(" P%-6d %-13d %-12d %-14d %-17d %-15d\n",
               pid[i], at[i], bt[i], wt[i], ct[i], tat[i]);
    }

    rr[0] = (double)wtsum / n;
    rr[1] = (double)tatsum / n;
}

int main() {
    int n;
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    int at[n], bt[n], pid[n];
    printf("Enter the arrival time, burst time of processes: \n");
    for (int i = 0; i < n; i++) {
        printf("Process %d: ", i + 1);
        scanf("%d %d", &at[i], &bt[i]);
        pid[i] = i + 1;
    }

    sortbyarrival(n, at, bt, pid);

    double rr[2];
    roundrobin(n, pid, at, bt, rr);

    printf("Average Waiting Time: %.2f\n", rr[0]);
    printf("Average Turnaround Time: %.2f\n", rr[1]);
    return 0;
}
