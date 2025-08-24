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

void sjfpremptive(int n, int *pid, int* at, int* bt, double* sjftask) {
    int completed = 0, time = 0;
    int ct[n], wt[n], tat[n], btr[n];
    for (int i = 0; i < n; i++) btr[i] = bt[i];

    int wtsum = 0, tatsum = 0;

    printf("Task    Arrival Time   Burst Time     Waiting Time   Completion Time   Turnaround Time \n");

    // For Gantt chart
    printf("\nGantt Chart:\n");
    int prev = -1; // track previous running process

    while (completed < n) {
        int j = -1, minbtr = 1e9;

        for (int i = 0; i < n; i++) {
            if (at[i] <= time && btr[i] > 0) {
                if (btr[i] < minbtr) {
                    minbtr = btr[i];
                    j = i;
                } else if (btr[i] == minbtr && at[i] < at[j]) {
                    j = i;
                }
            }
        }

        if (j == -1) {
            // CPU idle
            if (prev != -2) { // print "Idle" only once continuously
                printf("| %d Idle ", time);
                prev = -2;
            }
            time++;
            continue;
        }

        // Context switch detection
        if (prev != j) {
            printf("| %d P%d ", time, pid[j]);
            prev = j;
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

            printf("%d", time); // print end time when process finishes
        }
    }

    printf("|\n\n");

    // Table of processes
    for (int i = 0; i < n; i++) {
        printf(" P%-6d %-13d %-12d %-14d %-17d %-15d\n",
               pid[i], at[i], bt[i], wt[i], ct[i], tat[i]);
    }

    sjftask[0] = (double)wtsum / n;
    sjftask[1] = (double)tatsum / n;
}

int main() {
    int n;
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    printf("Enter the arrival time, burst time of processes: \n");
    int at[n], bt[n], pid[n];
    for (int i = 0; i < n; i++) {
        printf("Process %d: ", i + 1);
        scanf("%d %d", &at[i], &bt[i]);
        pid[i] = i + 1; 
    }
    sortbyarrival(n, at, bt, pid);
    double sjftask[2];
    sjfpremptive(n, pid, at, bt, sjftask);
    printf("Average Waiting Time: %.2f\nAverage Turnaround Time: %.2f\n", sjftask[0], sjftask[1]);
    return 0;
}
