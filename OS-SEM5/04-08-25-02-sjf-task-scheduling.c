#include <stdio.h>

void calculatesjf(int n, int* at, int* bt, double* sjf) {
    int completed = 0, time = 0;
    int ct[n], wt[n], tat[n], visited[n];
    int wtsum = 0, tatsum = 0;

    for (int i = 0; i < n; i++) visited[i] = 0; // 0 = not visited

    printf("Task    Arrival Time   Burst Time   Waiting Time   Completion Time   Turnaround Time\n");

    while (completed < n) {
        int j = -1;
        int minbt = 1e9;

        // Find the shortest job that has arrived
        for (int i = 0; i < n; i++) {
            if (!visited[i] && at[i] <= time) {
                if (bt[i] < minbt) {
                    minbt = bt[i];
                    j = i;
                }
                // Tie-breaker: if burst times are equal, choose earlier arrival
                else if (bt[i] == minbt && at[i] < at[j]) {
                    j = i;
                }
            }
        }

        if (j == -1) {
            // No process has arrived yet, jump to next arrival
            int nextarrival = 1e9;
            for (int i = 0; i < n; i++) {
                if (!visited[i] && at[i] < nextarrival) {
                    nextarrival = at[i];
                }
            }
            time = nextarrival;
            continue;
        }

        // Process execution
        time += bt[j];
        ct[j] = time;
        tat[j] = ct[j] - at[j];
        wt[j] = tat[j] - bt[j];
        visited[j] = 1;

        wtsum += wt[j];
        tatsum += tat[j];
        completed++;

        printf(" P%-6d %-13d %-12d %-14d %-17d %-15d\n",
               j + 1, at[j], bt[j], wt[j], ct[j], tat[j]);
    }

    sjf[0] = (double)wtsum / n;
    sjf[1] = (double)tatsum / n;
}

int main() {
    int n;
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    printf("Enter the arrival time & burst time of processes: \n");
    int at[n], bt[n], pid[n];
    for (int i = 0; i < n; i++) {
        printf("Process %d: ", i + 1);
        scanf("%d %d", &at[i], &bt[i]);
        pid[i] = i + 1; // Store original process ID
    }

    double sjf[2];.
    calculatesjf(n, at, bt, sjf);
    printf("Average Waiting Time: %.2f\nAverage Turnaround Time: %.2f\n", sjf[0], sjf[1]);
    return 0;
}
