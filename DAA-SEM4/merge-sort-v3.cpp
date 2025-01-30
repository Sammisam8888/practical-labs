#include <iostream>
#include <ctime>
using namespace std;

class Sort {
    int* arr;
    int n;
    string arrayTypes[4] = {"Sorted Ascending", "Sorted Descending", "Unsorted", "Sorted and Unsorted mixed"};

    void merge(int left, int mid, int right) {
        int n1 = mid - left + 1, n2 = right - mid;
        int* leftArr = new int[n1];
        int* rightArr = new int[n2];
        for (int i = 0; i < n1; i++) leftArr[i] = arr[left + i];
        for (int i = 0; i < n2; i++) rightArr[i] = arr[mid + 1 + i];
        int i = 0, j = 0, k = left;
        while (i < n1 && j < n2) arr[k++] = (leftArr[i] <= rightArr[j]) ? leftArr[i++] : rightArr[j++];
        while (i < n1) arr[k++] = leftArr[i++];
        while (j < n2) arr[k++] = rightArr[j++];
        delete[] leftArr;
        delete[] rightArr;
    }

    void mergeSort(int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            mergeSort(left, mid);
            mergeSort(mid + 1, right);
            merge(left, mid, right);
        }
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
    }

    double runSorting(string& type) {
        getdata(type);
        display("Before sorting:");

        clock_t start = clock();
        cout << "Start Time: " << double(start)/CLOCKS_PER_SEC << " seconds" << endl;
        mergeSort(0, n - 1);
        clock_t end = clock();
        cout << "End Time: " << double(end)/CLOCKS_PER_SEC << " seconds" << endl;

        display("After Sorting:");

        double time_taken = double(end - start) / CLOCKS_PER_SEC;
        cout << "Time taken: " << time_taken << " seconds\n\n";

        delete[] arr;
        return time_taken;
    }

public:
    void compareTimes() {  // No need for parameter anymore
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
        cout << "The test case with the minimum time: " << minType << " took " << minTime << " seconds.\n";
        cout << "The test case with the maximum time: " << maxType << " took " << maxTime << " seconds.\n";
    }
};

int main() {
    Sort s;
    s.compareTimes();  
    return 0;
}