#include <stdio.h>

void calculate_sjfs(int n, int* at, int* bt, double* sjfs) {
    int completed = 0, time = 0;
    int ct[n], wt[n], tat[n], visited[n];
    int wt_total = 0, tat_total = 0;

    for (int i = 0; i < n; i++) visited[i] = 0; // 0 = not visited

    printf("Task    Arrival Time   Burst Time   Waiting Time   Completion Time   Turnaround Time\n");

    while (completed < n) {
        int idx = -1;
        int min_bt = 1e9;

        // Find the shortest job that has arrived
        for (int i = 0; i < n; i++) {
            if (!visited[i] && at[i] <= time) {
                if (bt[i] < min_bt) {
                    min_bt = bt[i];
                    idx = i;
                }
                // Tie-breaker: if burst times are equal, choose earlier arrival
                else if (bt[i] == min_bt && at[i] < at[idx]) {
                    idx = i;
                }
            }
        }

        if (idx == -1) {
            // No process has arrived yet, jump to next arrival
            int next_arrival = 1e9;
            for (int i = 0; i < n; i++) {
                if (!visited[i] && at[i] < next_arrival) {
                    next_arrival = at[i];
                }
            }
            time = next_arrival;
            continue;
        }

        // Process execution
        time += bt[idx];
        ct[idx] = time;
        tat[idx] = ct[idx] - at[idx];
        wt[idx] = tat[idx] - bt[idx];
        visited[idx] = 1;

        wt_total += wt[idx];
        tat_total += tat[idx];
        completed++;

        printf(" P%-6d %-13d %-12d %-14d %-17d %-15d\n",
               idx + 1, at[idx], bt[idx], wt[idx], ct[idx], tat[idx]);
    }

    sjfs[0] = (double)wt_total / n;
    sjfs[1] = (double)tat_total / n;
}

int main() {
    int n;
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    int at[n], bt[n];
    for (int i = 0; i < n; i++) {
        printf("Enter the arrival time and burst time of process %d: ", i + 1);
        scanf("%d %d", &at[i], &bt[i]);
    }

    double sjfs[2];
    calculate_sjfs(n, at, bt, sjfs);
    printf("Average Waiting Time: %.2f\nAverage Turnaround Time: %.2f\n", sjfs[0], sjfs[1]);
    return 0;
}
