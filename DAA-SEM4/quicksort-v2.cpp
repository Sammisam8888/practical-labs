
// WAP to perform quick sort operation over an array and use the clock function to print the initial and final time taken for the entire quick sort operation
#include <iostream>
#include <ctime>
#include <string>
using namespace std;

class Sort {
private:
    int size, *array, pivotIndex, count = 0;
    double timeIntervals[12];
    bool pivotFlag = false;
    string arrayTypes[4] = {"Sorted Ascending array", "Sorted Descending Array", "Unsorted array", "Sorted and Unsorted mixed array"};

    void quicksort(int low, int high) {
        if (low >= high) return;

        if (pivotFlag) {
            pivotIndex = low; // Assume the pivot as 'low' index for subsequent iterations
        }

        int i = low + 1, j = high;

        while (i <= j) {
            while (i <= high && array[i] <= array[pivotIndex])
                i++;
            while (j >= low && array[j] > array[pivotIndex])
                j--;
            if (i < j) {
                swap(array[i], array[j]);
            }
        }

        pivotFlag = true;

        swap(array[pivotIndex], array[j]);
        quicksort(low, j - 1);
        quicksort(j + 1, high);
    }

    void displayArray() {
        cout << "The elements of the array are: " << endl;
        for (int i = 0; i < size; i++) {
            cout << array[i] << " ";
        }
        cout << endl;
    }

    void inputData(int typeIndex) {
        cout << "Enter values for a " << arrayTypes[typeIndex] << endl;
        cout << "Enter the size of the array: ";
        cin >> size;
        array = new int[size];
        cout << "Enter the elements of the array: ";
        for (int i = 0; i < size; i++) {
            cin >> array[i];
        }
        cout << "Enter the pivot element index: ";
        cin >> pivotIndex;
    }

    void calculateTime(clock_t start, clock_t end, int typeIndex) {
        timeIntervals[typeIndex * 3] = double(start) / CLOCKS_PER_SEC;
        timeIntervals[typeIndex * 3 + 1] = double(end) / CLOCKS_PER_SEC;
        timeIntervals[typeIndex * 3 + 2] = double(end - start) / CLOCKS_PER_SEC;
    }

    void displayTimeIntervals() {
        int slowest = 0, fastest = 0;
        cout << "The time differences between the 4 types of sorting are as follows:" << endl;

        for (int i = 0; i < 4; i++) {
            cout << "For " << arrayTypes[i] << ":" << endl;
            cout << "Initial time: " << timeIntervals[i * 3] << " seconds" << endl;
            cout << "Final time: " << timeIntervals[i * 3 + 1] << " seconds" << endl;
            cout << "Time taken: " << timeIntervals[i * 3 + 2] << " seconds" << endl;

            if (timeIntervals[i * 3 + 2] < timeIntervals[fastest * 3 + 2]) {
                fastest = i;
            }
            if (timeIntervals[i * 3 + 2] > timeIntervals[slowest * 3 + 2]) {
                slowest = i;
            }
        }

        cout << "According to the above comparison of time differences, " << arrayTypes[fastest]
             << " is taking the least time to perform quick sort, with a complexity of "
             << timeIntervals[fastest * 3 + 2] << " seconds." << endl;

        cout << "And " << arrayTypes[slowest]
             << " is taking the most time compared to others, with a complexity of "
             << timeIntervals[slowest * 3 + 2] << " seconds." << endl;
    }

public:
    void runOperations() {
        for (int i = 0; i < 4; i++) {
            inputData(i);
            cout << "Before sorting: " << endl;
            displayArray();

            clock_t startTime = clock(); // Start time

            quicksort(0, size - 1);

            clock_t endTime = clock(); // End time

            cout << "After Sorting: " << endl;
            displayArray();

            calculateTime(startTime, endTime, i);

            delete[] array;
        }
        displayTimeIntervals();
    }
};

int main() {
    Sort qs;
    qs.runOperations();
    return 0;
}
