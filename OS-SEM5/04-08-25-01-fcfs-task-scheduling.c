#include <stdio.h>

void sort_by_arrival(int n, int* at, int* bt, int* pid) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (at[j] < at[i]) {
                // Swap arrival times
                int temp = at[i];
                at[i] = at[j];
                at[j] = temp;
                // Swap burst times
                temp = bt[i];
                bt[i] = bt[j];
                bt[j] = temp;
                // Swap process IDs
                temp = pid[i];
                pid[i] = pid[j];
                pid[j] = temp;
            }
        }
    }
}

void calculatefcfs(int n, int* at, int* bt, int* pid, double* fcfs) {
    int wt_total = 0, tat_total = 0;
    int ct[n], wt[n], tat[n];

    int time = 0;
    printf("Task    Arrival Time   Burst Time   Waiting Time   Completion Time   Turnaround Time\n");

    for (int i = 0; i < n; i++) {
        if (time < at[i])  // If CPU is idle
            time = at[i];

        time += bt[i];           // Process runs
        ct[i] = time;            // Completion time
        tat[i] = ct[i] - at[i];  // Turnaround time
        wt[i] = tat[i] - bt[i];  // Waiting time

        wt_total += wt[i];
        tat_total += tat[i];

        printf(" P%-2d      %2d             %2d             %2d             %2d             %2d\n",
               pid[i], at[i], bt[i], wt[i], ct[i], tat[i]);
    }

    fcfs[0] = (double)wt_total / n;
    fcfs[1] = (double)tat_total / n;
}

int main() {
    int n;
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    int at[n], bt[n], pid[n];
    for (int i = 0; i < n; i++) {
        printf("Enter the arrival time and burst time of process %d: ", i + 1);
        scanf("%d %d", &at[i], &bt[i]);
        pid[i] = i + 1; // Store original process ID
    }

    // Sort processes by arrival time but keep process IDs
    sort_by_arrival(n, at, bt, pid);

    double fcfs[2];
    calculatefcfs(n, at, bt, pid, fcfs);
    printf("Average Waiting Time: %.2f\nAverage Turnaround Time: %.2f\n", fcfs[0], fcfs[1]);
    return 0;
}
