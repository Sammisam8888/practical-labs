#include <iostream>
using namespace std;

class Operation {
    int n, k, target, *arr;

    // Private function for quicksort and partition
    void quicksort(int low, int high);
    int partition(int low, int high);

public:
    void getdata();
    void klargest();
    void display();
};

// Function to input array data
void Operation::getdata() {
    cout << "Enter the size of the array: ";
    cin >> n;

    // Dynamically allocate memory for the array
    arr = new int[n];

    cout << "Enter the elements of the array: " << endl;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << "Enter the value of k: ";
    cin >> k;
}

// Function to find the kth largest element using quicksort
void Operation::klargest() {
    if (k > n) {
        cout << "Error: k cannot be greater than n" << endl;
        return;
    }

    quicksort(0, n - 1);   // Sort the array
    target = arr[n - k];   // kth largest element is at index n-k
}

// Quicksort algorithm
void Operation::quicksort(int low, int high) {
    if (low < high) {
        int pi = partition(low, high);  // Partition the array and get pivot index
        quicksort(low, pi - 1);         // Sort the left half
        quicksort(pi + 1, high);        // Sort the right half
    }
}

// Partition function to rearrange elements based on the pivot
int Operation::partition(int low, int high) {
    int pivot = arr[high];  // Choose the last element as the pivot
    int i = low - 1;        // Index of the smaller element

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }

    swap(arr[i + 1], arr[high]);  // Place pivot at the correct position
    return i + 1;
}

// Function to display the kth largest element
void Operation::display() {
    cout << "The " << k << "th largest element in the array is: " << target << endl;
}

int main() {
    Operation op;
    op.getdata();
    op.klargest();
    op.display();
    return 0;
}

