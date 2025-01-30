#include <iostream>
#include <ctime>
using namespace std;

class Sort {
    int* arr;
    int n;
    int pivotIndex;
    bool pivotFlag = false;
    string arrayTypes[4] = {"Sorted Ascending", "Sorted Descending", "Unsorted", "Sorted and Unsorted mixed"};

    void quickSort(int low, int high) {
        if (low >= high) return;

        if (pivotFlag) {
            pivotIndex = low;
        }

        int i = low + 1, j = high;

        while (i <= j) {
            while (i <= high && arr[i] <= arr[pivotIndex])
                i++;
            while (j >= low && arr[j] > arr[pivotIndex])
                j--;
            if (i < j) {
                swap(arr[i], arr[j]);
            }
        }

        pivotFlag = true;
        swap(arr[pivotIndex], arr[j]);
        quickSort(low, j - 1);
        quickSort(j + 1, high);
    }

    void display(string message = "") {
        if (!message.empty()) {
            cout << message << "\n";
        }
        cout << "The elements of the array are: ";
        for (int i = 0; i < n; i++) {
            cout << arr[i] << " ";
        }
        cout << "\n";
    }

    void getdata(string& type) {
        cout << "Enter values for a " << type << " array\nEnter the size of the array: ";
        cin >> n;
        arr = new int[n];
        cout << "Enter the elements of the array: ";
        for (int i = 0; i < n; i++) cin >> arr[i];
        cout << "Enter the pivot element index: ";
        cin >> pivotIndex;
    }

    double runSorting(string& type) {
        getdata(type);
        display("Before sorting:");

        clock_t start = clock();
        cout << "Start Time: " << double(start)/CLOCKS_PER_SEC << " seconds" << endl;
        
        pivotFlag = false;
        quickSort(0, n - 1);
        
        clock_t end = clock();
        cout << "End Time: " << double(end)/CLOCKS_PER_SEC << " seconds" << endl;

        display("After Sorting:");

        double time_taken = double(end - start) / CLOCKS_PER_SEC;
        cout << "Time taken: " << time_taken << " seconds\n\n";

        delete[] arr;
        return time_taken;
    }

public:
    void compareTimes() {
        double minTime = 1e9;
        double maxTime = 0.0;
        string minType, maxType;
        
        for (int i = 0; i < 4; i++) {
            double timeTaken = runSorting(arrayTypes[i]);
            if (timeTaken < minTime) {
                minTime = timeTaken;
                minType = arrayTypes[i];
            }
            if (timeTaken > maxTime) {
                maxTime = timeTaken;
                maxType = arrayTypes[i];
            }
        }
        displayResults(minType, minTime, maxType, maxTime);
    }

    void displayResults(string minType, double minTime, string maxType, double maxTime) {
        cout << "The test with the minimum time: " << minType << " took " << minTime << " seconds.\n";
        cout << "The test with the maximum time: " << maxType << " took " << maxTime << " seconds.\n";
    }
};

int main() {
    Sort s;
    s.compareTimes();
    return 0;
}