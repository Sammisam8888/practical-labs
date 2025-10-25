#include <stdio.h>

int findLRU(int time[], int n) {
    int min = time[0], pos = 0;
    for (int i = 1; i < n; i++) {
        if (time[i] < min) {
            min = time[i];
            pos = i;
        }
    }
    return pos;
}

int findMRU(int time[], int n) {
    int max = time[0], pos = 0;
    for (int i = 1; i < n; i++) {
        if (time[i] > max) {
            max = time[i];
            pos = i;
        }
    }
    return pos;
}

void fifo(int pages[], int n, int frames) {
    int frame[frames], front = 0, count = 0, faults = 0;
    printf("\nFIFO Page Replacement:\n");
    for (int i = 0; i < frames; i++) frame[i] = -1;

    for (int i = 0; i < n; i++) {
        int found = 0;
        for (int j = 0; j < frames; j++) {
            if (frame[j] == pages[i]) {
                found = 1;
                break;
            }
        }

        if (!found) {
            frame[front] = pages[i];
            front = (front + 1) % frames;
            faults++;
        }

        printf("Page %2d -> ", pages[i]);
        for (int j = 0; j < frames; j++)
            if (frame[j] != -1) printf("%d ", frame[j]);
            else printf("- ");
        printf("\n");
    }
    printf("Total Page Faults (FIFO): %d\n", faults);
}

void lru(int pages[], int n, int frames) {
    int frame[frames], time[frames], count = 0, faults = 0;
    printf("\nLRU Page Replacement:\n");
    for (int i = 0; i < frames; i++) frame[i] = -1;

    for (int i = 0; i < n; i++) {
        int found = 0;
        for (int j = 0; j < frames; j++) {
            if (frame[j] == pages[i]) {
                found = 1;
                time[j] = count++;
                break;
            }
        }

        if (!found) {
            int pos;
            for (pos = 0; pos < frames; pos++)
                if (frame[pos] == -1) break;

            if (pos == frames)
                pos = findLRU(time, frames);

            frame[pos] = pages[i];
            time[pos] = count++;
            faults++;
        }

        printf("Page %2d -> ", pages[i]);
        for (int j = 0; j < frames; j++)
            if (frame[j] != -1) printf("%d ", frame[j]);
            else printf("- ");
        printf("\n");
    }
    printf("Total Page Faults (LRU): %d\n", faults);
}

void mru(int pages[], int n, int frames) {
    int frame[frames], time[frames], count = 0, faults = 0;
    printf("\nMRU (Most Recently Used) Page Replacement:\n");
    for (int i = 0; i < frames; i++) frame[i] = -1;

    for (int i = 0; i < n; i++) {
        int found = 0;
        for (int j = 0; j < frames; j++) {
            if (frame[j] == pages[i]) {
                found = 1;
                time[j] = count++;
                break;
            }
        }

        if (!found) {
            int pos;
            for (pos = 0; pos < frames; pos++)
                if (frame[pos] == -1) break;

            if (pos == frames)
                pos = findMRU(time, frames);

            frame[pos] = pages[i];
            time[pos] = count++;
            faults++;
        }

        printf("Page %2d -> ", pages[i]);
        for (int j = 0; j < frames; j++)
            if (frame[j] != -1) printf("%d ", frame[j]);
            else printf("- ");
        printf("\n");
    }
    printf("Total Page Faults (MRU): %d\n", faults);
}

int main() {
    int n, frames;

    printf("Enter number of pages: ");
    scanf("%d", &n);
    int pages[n];
    printf("Enter page reference string:");
    for (int i = 0; i < n; i++) scanf("%d", &pages[i]);

    printf("Enter number of frames: ");
    scanf("%d", &frames);

    fifo(pages, n, frames);
    lru(pages, n, frames);
    mru(pages, n, frames);

    return 0;
}
