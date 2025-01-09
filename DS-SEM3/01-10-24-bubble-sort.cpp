#include <iostream>
using namespace std;

class Sorting {
    int *arr, n;

public:
    Sorting() {
        cout << "Enter the size of the array: ";
        cin >> n;
        arr = new int[n];
        cout << "Enter the elements of the array: ";
        for (int i = 0; i < n; i++)
            cin >> arr[i];
    }

    void display() {
        cout << "The elements of the array are: ";
        for (int i = 0; i < n; i++)
            cout << arr[i] << " ";
        cout << endl;
    }

    void bubblesort() {
        for (int i = 0; i < n - 1; i++) {
            bool swapped = true;
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr[j], arr[j + 1]);
                    swapped = false; // Set swapped to false to indicate a swap occurred
                }
            }
            if (swapped) { // If no swaps were made, array is sorted
                break;
            }
        }
        cout << "Array has been sorted" << endl;
    }
};

int main() {
    Sorting st;
    st.bubblesort();
    st.display();
    return 0;
}
