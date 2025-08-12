#include <stdio.h>

void swap (int a, int b){
    a=a+b;
    b=a-b;
    a=a-b;
}

void sortbyarrival(int n, int* at, int* bt, int* pr, int* pid) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (at[j] < at[i]) {
                swap(at[i],at[j]);
                swap(bt[i],bt[j]);
                swap(pid[i],pid[j]);
                swap(pr[i],pr[j]);
            }
        }
    }
}

void priorityscheduling(int n, int *pid, int* at, int* bt,int* pr, double* prtask) {
    int completed = 0, time = 0;
    int ct[n], wt[n], tat[n], visited[n];
    int wtsum = 0, tatsum = 0;

    for (int i = 0; i < n; i++) visited[i] = 0; 

    printf("Task    Arrival Time   Burst Time   Priority     Waiting Time   Completion Time   Turnaround Time \n");

    while (completed < n) {
        int j = -1;
        for (int i = 0; i < n; i++) {
            if (!visited[i] && at[i] <= time) {
                if (j == -1 || pr[i] < pr[j]) {
                    j = i;
                }
            }
        }

        if (j == -1) {
            int nextarrival = 1e9;
            for (int i = 0; i < n; i++) {
                if (!visited[i] && at[i] < nextarrival) {
                    nextarrival = at[i];
                }
            }
            time = nextarrival;
            continue;
        }

        time += bt[j];
        ct[j] = time;
        tat[j] = ct[j] - at[j];
        wt[j] = tat[j] - bt[j];
        visited[j] = 1;

        wtsum += wt[j];
        tatsum += tat[j];
        completed++;

        printf(" P%-6d %-13d %-12d %-12d %-14d %-17d %-15d\n",
               pid[j], at[j], bt[j], pr[j], wt[j], ct[j], tat[j]);
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
    sortbyarrival(n,at,bt,pr,pid);
    double prtask[2];
    priorityscheduling(n, pid, at, bt, pr, prtask);
    printf("Average Waiting Time: %.2f\nAverage Turnaround Time: %.2f\n", prtask[0], prtask[1]);
    return 0;
}
