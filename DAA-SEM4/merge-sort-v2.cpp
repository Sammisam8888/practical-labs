#include <iostream>
#include <ctime>
#include <string>
#include <climits>
using namespace std;

class MergeSort {
private:
    int arrSize, *dataArray;
    double timeDiffs[12];
    string arrayTypes[4] = {"Sorted Ascending array", "Sorted Descending Array", "Unsorted array", "Sorted and Unsorted mixed array"};

    void mergeSort(int left, int right) {
        if (left >= right) return;

        int middle = left + (right - left) / 2;

        // Recursively sort the left and right halves
        mergeSort(left, middle);
        mergeSort(middle + 1, right);

        // Merge the sorted halves
        merge(left, middle, right);
    }

    void merge(int left, int middle, int right) {
        int leftSize = middle - left + 1;
        int rightSize = right - middle;

        // Temporary arrays for left and right halves
        int* leftArray = new int[leftSize];
        int* rightArray = new int[rightSize];

        for (int i = 0; i < leftSize; i++) {
            leftArray[i] = dataArray[left + i];
        }
        for (int i = 0; i < rightSize; i++) {
            rightArray[i] = dataArray[middle + 1 + i];
        }

        int i = 0, j = 0, k = left;

        // Merge the arrays back into the main array
        while (i < leftSize && j < rightSize) {
            if (leftArray[i] <= rightArray[j]) {
                dataArray[k++] = leftArray[i++];
            } else {
                dataArray[k++] = rightArray[j++];
            }
        }

        // Copy remaining elements, if any
        while (i < leftSize) {
            dataArray[k++] = leftArray[i++];
        }
        while (j < rightSize) {
            dataArray[k++] = rightArray[j++];
        }

        delete[] leftArray;
        delete[] rightArray;
    }

    void displayArray() {
        cout << "The elements of the array are: " << endl;
        for (int i = 0; i < arrSize; i++) {
            cout << dataArray[i] << " ";
        }
        cout << endl;
    }

    void inputArrayData(int typeIndex) {
        cout << "Enter values for a " << arrayTypes[typeIndex] << endl;
        cout << "Enter the size of the array: ";
        cin >> arrSize;
        dataArray = new int[arrSize];
        cout << "Enter the elements of the array: ";
        for (int i = 0; i < arrSize; i++) {
            cin >> dataArray[i];
        }
    }

    void calculateTime(clock_t startTime, clock_t endTime, int typeIndex) {
        timeDiffs[typeIndex * 3] = double(startTime) / CLOCKS_PER_SEC;
        timeDiffs[typeIndex * 3 + 1] = double(endTime) / CLOCKS_PER_SEC;
        timeDiffs[typeIndex * 3 + 2] = double(endTime - startTime) / CLOCKS_PER_SEC;
    }

    void displayTimeDiffs() {
        int slowest = 0, fastest = 0; // Indices for slowest and fastest types
        cout << "The time differences between the 4 types of sorting are as follows:" << endl;

        for (int i = 0; i < 4; i++) {
            cout << "For " << arrayTypes[i] << ":" << endl;
            cout << "Initial time: " << timeDiffs[i * 3] << " seconds" << endl;
            cout << "Final time: " << timeDiffs[i * 3 + 1] << " seconds" << endl;
            cout << "Time taken: " << timeDiffs[i * 3 + 2] << " seconds" << endl;

            if (timeDiffs[i * 3 + 2] < timeDiffs[fastest * 3 + 2]) {
                fastest = i;
            }
            if (timeDiffs[i * 3 + 2] > timeDiffs[slowest * 3 + 2]) {
                slowest = i;
            }
        }

        // Output the fastest and slowest cases
        cout << "According to the above comparison of time differences, " << arrayTypes[fastest]
             << " is taking the least time to perform merge sort, with a complexity of "
             << timeDiffs[fastest * 3 + 2] << " seconds." << endl;

        cout << "And " << arrayTypes[slowest]
             << " is taking the most time compared to others, with a complexity of "
             << timeDiffs[slowest * 3 + 2] << " seconds." << endl;
    }

public:
    void performOperations() {
        for (int i = 0; i < 4; i++) {
            inputArrayData(i);
            cout << "Before sorting: " << endl;
            displayArray();

            clock_t startTime = clock(); // Start time

            mergeSort(0, arrSize - 1);

            clock_t endTime = clock(); // End time

            cout << "After Sorting: " << endl;
            displayArray();

            calculateTime(startTime, endTime, i);

            delete[] dataArray;
        }
        displayTimeDiffs();
    }
};

int main() {
    MergeSort sorter;
    sorter.performOperations();
    return 0;
}