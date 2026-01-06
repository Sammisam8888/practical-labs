#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i, head, total = 0, completed = 0;

    printf("Enter number of disk requests: ");
    scanf("%d", &n);

    int req[n], visited[n];
    printf("Enter the disk request sequence:\n");
    for (i = 0; i < n; i++) {
        scanf("%d", &req[i]);
        visited[i] = 0;
    }

    printf("Enter initial head position: ");
    scanf("%d", &head);

    printf("\nSequence of Head Movement:\n");
    printf("%d", head);

    while (completed < n) {
        int min_dist = 9999, index = -1;

        for (i = 0; i < n; i++) {
            if (!visited[i]) {
                int dist = abs(req[i] - head);
                if (dist < min_dist) {
                    min_dist = dist;
                    index = i;
                }
            }
        }

        visited[index] = 1;
        total += abs(req[index] - head);
        head = req[index];
        completed++;

        printf(" -> %d", head);
    }

    printf("\n\nTotal Head Movement = %d\n", total);
    printf("Average Head Movement = %.2f\n", (float)total / n);

    return 0;
}
