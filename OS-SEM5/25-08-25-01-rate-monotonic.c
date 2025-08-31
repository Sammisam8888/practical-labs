#include <stdio.h>  
  
// Utility function to swap two integers  
void swap(int *a, int *b) {  
    int temp = *a;  
    *a = *b;  
    *b = temp;  
}  
  
// Sorts tasks based on their periods (shortest period first)  
void sortbyperiod(int n, int* p, int* bt, int* pid) {  
    for (int i = 0; i < n - 1; i++) {  
        for (int j = i + 1; j < n; j++) {  
            if (p[j] < p[i]) {  
                swap(&p[i], &p[j]);  
                swap(&bt[i], &bt[j]);  
                swap(&pid[i], &pid[j]);  
            }  
        }  
    }  
}  
  
// Rate Monotonic Scheduling (Preemptive)  
void ratesmonotonic(int n, int* pid, int* p, int* bt, double* rmstask) {  
    int time = 0;  
    int firstinstance = 0;  
    int ct[n], wt[n], tat[n];  
    double wtsum = 0, tatsum = 0;  
  
    // btr stores the remaining burst time for the *current* job of a task.  
    // A value of 0 means no active job or the current job is finished.  
    int btr[n];  
    for(int i = 0; i < n; i++) btr[i] = 0;  
      
    // arrivalfirst is 0 for all tasks in this model.  
    int arrivalfirst[n];  
    for(int i = 0; i < n; i++) arrivalfirst[i] = 0;  
  
    // A flag to ensure we only calculate stats once for the first instance of each task.  
    int check[n];  
    for(int i = 0; i < n; i++) check[i] = 0;  
  
    printf("\nGantt Chart:\n");  
    int prev = -1; // Track previous running process to detect context switches  
  
    // Loop until the first instance of every task has been completed.  
    // An upper time limit prevents infinite loops for unschedulable task sets.  
    while(firstinstance < n && time < 200) {  
  
        // 1. At the current 'time', check for new job arrivals for all tasks.  
        for (int i = 0; i < n; i++) {  
            if (time % p[i] == 0) {  
                btr[i] = bt[i]; // A new job arrives with its full burst time.  
            }  
        }  
  
        // 2. Select the highest-priority task that has work to do.  
        // Since tasks are pre-sorted by period, the first task found is the one.  
        int j = -1; // Index of the task to run  
        for (int i = 0; i < n; i++) {  
            if (btr[i] > 0) {  
                j = i;  
                break;  
            }  
        }  
  
        // 3. Execute the selected task or handle idle time.  
        if (j != -1) { // A task is ready to run  
            // Print to Gantt chart if context has switched  
            if (prev != j) {  
                printf("| %d P%d ", time, pid[j]);  
                prev = j;  
            }  
              
            btr[j]--; // Run for one time unit  
            time++;  
  
            // Check if the job that just ran has now finished  
            if (btr[j] == 0) {  
                 printf("%d", time); // Print end time in Gantt chart  
                   
                 // If this was the first instance of the task, calculate its stats.  
                 if (!check[j]) {  
                     firstinstance++;  
                     ct[j] = time;  
                     tat[j] = ct[j] - arrivalfirst[j];  
                     wt[j] = tat[j] - bt[j];  
                     wtsum += wt[j];  
                     tatsum += tat[j];  
                     check[j] = 1;  
                 }  
            }  
        } else { // No task is ready, CPU is idle  
            if (prev != -2) {  
                printf("| %d Idle ", time);  
                prev = -2;  
            }  
            time++;  
        }  
    }  
  
    printf("|\n\n");  
    printf("Task    Period         Burst Time   Waiting Time   Completion Time   Turnaround Time \n");  
  
    // Table of processes  
    for (int i = 0; i < n; i++) {  
        printf(" P%-6d %-13d %-12d %-14d %-17d %-15d\n",  
               pid[i], p[i], bt[i], wt[i], ct[i], tat[i]);  
    }  
  
    rmstask[0] = wtsum / n;  
    rmstask[1] = tatsum / n;  
}  
  
int main() {  
    int n;  
    printf("Enter the number of processes: ");  
    scanf("%d", &n);  
  
    printf("Enter the burst time and period of processes: \n");  
    int bt[n], p[n], pid[n];  
    for (int i = 0; i < n; i++) {  
        printf("Process %d: ", i + 1);  
        scanf("%d %d", &bt[i], &p[i]);  
        pid[i] = i + 1;  
    }  
  
    sortbyperiod(n, p, bt, pid);  
  
    double rmstask[2];  
    ratesmonotonic(n, pid, p, bt, rmstask);  
  
    printf("Average Waiting Time: %.2f\nAverage Turnaround Time: %.2f\n", rmstask[0], rmstask[1]);  
      
    return 0;  
}  
