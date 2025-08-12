#include <stdio.h>

void sortbyarrival(int n, int* at, int* bt, int* pid) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (at[j] < at[i]) {
                
                int temp = at[i];
                at[i] = at[j];
                at[j] = temp;
                
                temp = bt[i];
                bt[i] = bt[j];
                bt[j] = temp;
                
                temp = pid[i];
                pid[i] = pid[j];
                pid[j] = temp;
            }
        }
    }
}

void calculatefcfs(int n, int* at, int* bt, int* pid, double* fcfs) {
    int wtsum = 0, tatsum = 0;
    int ct[n], wt[n], tat[n];

    int time = 0;
    printf("Task    Arrival Time   Burst Time   Waiting Time   Completion Time   Turnaround Time\n");

    for (int i = 0; i < n; i++) {
        if (time < at[i])  
            time = at[i];

        time += bt[i];           
        ct[i] = time;            
        tat[i] = ct[i] - at[i];  
        wt[i] = tat[i] - bt[i];  

        wtsum += wt[i];
        tatsum += tat[i];

        printf(" P%-6d %-13d %-12d %-14d %-17d %-15d\n",
               pid[i], at[i], bt[i], wt[i], ct[i], tat[i]);
    }

    fcfs[0] = (double)wtsum / n;
    fcfs[1] = (double)tatsum / n;
}

int main() {
    int n;
    printf("Enter the number of processes: ");
    scanf("%d", &n);
    printf("Enter the arrival time & burst time of processes: ");
    int at[n], bt[n], pid[n];
    for (int i = 0; i < n; i++) {
        printf("Process %d: ", i + 1);
        scanf("%d %d", &at[i], &bt[i]);
        pid[i] = i + 1; 
    }

    
    sortbyarrival(n, at, bt, pid);

    double fcfs[2];
    calculatefcfs(n, at, bt, pid, fcfs);
    printf("Average Waiting Time: %.2f\nAverage Turnaround Time: %.2f\n", fcfs[0], fcfs[1]);
    return 0;
}
