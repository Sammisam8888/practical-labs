#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Rate Monotonic Scheduling
void rateMonotonic(int n, int *pid, int *et, int *pt, int hyperPeriod) {
    int time = 0;
    int remaining[n], nextArrival[n], ct[n], wt[n], tat[n];
    int completed[n];

    for (int i = 0; i < n; i++) {
        remaining[i] = et[i];
        nextArrival[i] = 0;
        completed[i] = 0;
    }

    int wtsum = 0, tatsum = 0;

    printf("\nGantt Chart:\n");
    int prev = -1;

    while (time < hyperPeriod) {
        int j = -1, minPeriod = 1e9;

        for (int i = 0; i < n; i++) {
            if (time >= nextArrival[i] && remaining[i] > 0) {
                if (pt[i] < minPeriod) {
                    minPeriod = pt[i];
                    j = i;
                }
            }
        }

        if (j == -1) {
            if (prev != -2) {
                printf("| %d Idle ", time);
                prev = -2;
            }
            time++;
            continue;
        }

        if (prev != j) {
            printf("| %d P%d ", time, pid[j]);
            prev = j;
        }

        remaining[j]--;
        time++;

        if (remaining[j] == 0) {
            completed[j]++;
            ct[j] = time;
            tat[j] = ct[j] - (nextArrival[j]);
            wt[j] = tat[j] - et[j];
            wtsum += wt[j];
            tatsum += tat[j];

            nextArrival[j] += pt[j]; 
            remaining[j] = et[j];    
        }
    }
    printf("| %d |\n", time);

    printf("\nTask    ExecTime   Period   Waiting Time   Completion Time   Turnaround Time\n");
    for (int i = 0; i < n; i++) {
        printf(" P%-6d %-10d %-8d %-14d %-17d %-15d\n",
               pid[i], et[i], pt[i], wt[i], ct[i], tat[i]);
    }

    printf("Average Waiting Time: %.2f\n", (double)wtsum / n);
    printf("Average Turnaround Time: %.2f\n", (double)tatsum / n);
}

int gcd(int a, int b) {
    return (b == 0) ? a : gcd(b, a % b);
}

int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int main() {
    int n;
    printf("Enter number of processes: ");
    scanf("%d", &n);

    int pid[n], et[n], pt[n];
    for (int i = 0; i < n; i++) {
        printf("Process %d (ExecTime Period): ", i + 1);
        scanf("%d %d", &et[i], &pt[i]);
        pid[i] = i + 1;
    }

    // Calculate hyper-period (LCM of periods)
    int hyperPeriod = pt[0];
    for (int i = 1; i < n; i++) {
        hyperPeriod = lcm(hyperPeriod, pt[i]);
    }

    rateMonotonic(n, pid, et, pt, hyperPeriod);
    return 0;
}
