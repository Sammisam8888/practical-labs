#include <iostream>
using namespace std;

class Sorting {
    int *arr, n;

public:
    void getdata() {
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

    void selectionsort() {
        for (int i = 0; i < n - 1; i++) {
            int min_index = i; // Assume the minimum is the first element
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[min_index]) {
                    min_index = j; // Update the index of the minimum element
                }
            }
            swap(arr[min_index], arr[i]); // Swap the minimum element with the current element
        }
        cout << "Array has been sorted" << endl;
    }
};

int main() {
    Sorting st;
    st.getdata();
    st.selectionsort();
    st.display();
    return 0;
}
