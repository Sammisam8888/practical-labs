#include <iostream>
#include <ctime>

using namespace std;

void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1, n2 = right - mid;
    int leftArr[n1], rightArr[n2];
    
    for (int i = 0; i < n1; i++) leftArr[i] = arr[left + i];
    for (int i = 0; i < n2; i++) rightArr[i] = arr[mid + 1 + i];
    
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) arr[k++] = (leftArr[i] <= rightArr[j]) ? leftArr[i++] : rightArr[j++];
    while (i < n1) arr[k++] = leftArr[i++];
    while (j < n2) arr[k++] = rightArr[j++];
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

void runSortingTest(const string &type) {
    int n;
    cout << "Enter values for a " << type << " array\nEnter the size of the array: ";
    cin >> n;
    int arr[n];
    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) cin >> arr[i];
    
    cout << "Before sorting:\nThe elements of the array are: ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << "\n";
    
    clock_t start = clock();
    mergeSort(arr, 0, n - 1);
    clock_t end = clock();
    
    cout << "After Sorting:\nThe elements of the array are: ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << "\n";
    
    double time_taken = double(end - start) / CLOCKS_PER_SEC;
    cout << "Time taken: " << time_taken << " seconds\n\n";
}

int main() {
    runSortingTest("Sorted Ascending");
    runSortingTest("Sorted Descending");
    runSortingTest("Unsorted");
    runSortingTest("Sorted and Unsorted mixed");
    return 0;
}