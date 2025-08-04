#include <stdio.h>

void calculatefcfs(int n, int* at, int* bt,double* fcfs){
    int wt=0,ct=0,tat=0;
    printf("Task   Waiting Time     Completion Time    Turnaround Time   \n");
    for (int i=0;i<n;i++){
        wt+=ct-at[i];
        ct+=bt[i];
        tat+=ct-at[i];
        printf(" %d         %2d               %2d                 %2d\n",i+1,wt,ct,ct-at[i]);
    }
    double avgwt=(double)wt/n,avgtat=(double)tat/n;
    fcfs[0]=avgwt;fcfs[1]=avgtat;
}

int main(){
    int n;
    printf("Enter the number of processes: ");
    scanf("%d",&n);
    int at[n],bt[n];
    for (int i=0;i<n;i++){
        printf("Enter the arrival time and burst time of process %d: ",i+1);
        scanf("%d %d",&at[i],&bt[i]);
    }
    double fcfs[2];
    calculatefcfs(n,at,bt,fcfs);
    printf("Average Waiting Time: %f\nAverage Turnaround Time: %f\n",*fcfs,*(fcfs+1));
    return 0;
}