#include <iostream>
using namespace std;

class Operation {
    int n, k, target, *arr;

    // Private function for quicksort and partition
    void quicksort(int low, int high);
    
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
        exit(0);
    }

    quicksort(0, n - 1);   // Sort the array
    target = arr[n - k];   // kth largest element is at index n-k
}

void Operation::quicksort(int low, int high) {
    if (low >= high) return;  // Base case for recursion

    int pivot = arr[low];
    int i = low, j = high;
    
    while (i < j) {
        while (i < j && arr[j] >= pivot) j--;  // Find element smaller than pivot
        if (i < j) arr[i++] = arr[j];          // Move smaller element to left
        
        while (i < j && arr[i] <= pivot) i++;  // Find element larger than pivot
        if (i < j) arr[j--] = arr[i];          // Move larger element to right
    }
    
    arr[i] = pivot;  // Place pivot in the correct position
    
    quicksort(low, i - 1);   // Recursively sort left side
    quicksort(i + 1, high);  // Recursively sort right side
}

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
