#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void sortbyarrival(int n, int* at, int* bt, int* pr, int* pid) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (at[j] < at[i]) {
                swap(&at[i], &at[j]);
                swap(&bt[i], &bt[j]);
                swap(&pid[i], &pid[j]);
                swap(&pr[i], &pr[j]);
            }
        }
    }
}

void prioritypremptive(int n, int *pid, int* at, int* bt, int* pr, double* prtask) {
    int completed = 0, time = 0;
    int ct[n], wt[n], tat[n], btr[n];
    for (int i = 0; i < n; i++) btr[i] = bt[i];

    int wtsum = 0, tatsum = 0;

    printf("Task    Arrival Time   Burst Time   Priority     Waiting Time   Completion Time   Turnaround Time \n");

    while (completed < n) {
        int j = -1, priority = 1e9;
        for (int i = 0; i < n; i++) {
            if (at[i] <= time && btr[i] > 0) {
                if (pr[i] < priority) {
                    priority = pr[i];
                    j = i;
                }
            }
        }

        if (j == -1) {
            time++;
            continue;
        }

        btr[j]--;
        time++;

        if (btr[j] == 0) {
            completed++;
            ct[j] = time;
            tat[j] = ct[j] - at[j];
            wt[j] = tat[j] - bt[j];
            wtsum += wt[j];
            tatsum += tat[j];

            printf(" P%-6d %-13d %-12d %-12d %-14d %-17d %-15d\n",
                   pid[j], at[j], bt[j], pr[j], wt[j], ct[j], tat[j]);
        }
    }

    prtask[0] = (double)wtsum / n;
    prtask[1] = (double)tatsum / n;
}

int main() {
    int n;
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    printf("Enter the arrival time, burst time & priority of processes: \n");
    int at[n], bt[n], pid[n], pr[n];
    for (int i = 0; i < n; i++) {
        printf("Process %d: ", i + 1);
        scanf("%d %d %d", &at[i], &bt[i], &pr[i]);
        pid[i] = i + 1; 
    }
    sortbyarrival(n, at, bt, pr, pid);
    double prtask[2];
    prioritypremptive(n, pid, at, bt, pr, prtask);
    printf("Average Waiting Time: %.2f\nAverage Turnaround Time: %.2f\n", prtask[0], prtask[1]);
    return 0;
}
