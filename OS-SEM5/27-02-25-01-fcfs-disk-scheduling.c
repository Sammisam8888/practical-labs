#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i, head, total = 0;

    printf("Enter number of disk requests: ");
    scanf("%d", &n);

    int req[n];
    printf("Enter the disk request sequence:\n");
    for (i = 0; i < n; i++) {
        scanf("%d", &req[i]);
    }

    printf("Enter initial head position: ");
    scanf("%d", &head);

    printf("\nSequence of Head Movement:\n");
    printf("%d", head);

    for (i = 0; i < n; i++) {
        total += abs(req[i] - head);
        head = req[i];
        printf(" -> %d", head);
    }

    printf("\n\nTotal Head Movement = %d\n", total);
    printf("Average Head Movement = %.2f\n", (float)total / n);

    return 0;
}
