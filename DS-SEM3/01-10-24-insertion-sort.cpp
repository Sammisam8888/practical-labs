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

    void insertionsort() {
        for (int i = 1; i < n; i++) {
            int j = i;
            while (j > 0 && arr[j - 1] > arr[j]) {
                // Swap without using a temporary variable
                arr[j] += arr[j - 1];
                arr[j - 1] = arr[j] - arr[j - 1];
                arr[j] -= arr[j - 1];
                j--;
            }
        }
        cout << "Array has been sorted" << endl;
    }
};

int main() {
    Sorting st;
    st.getdata();
    st.insertionsort();
    st.display();
    return 0;
}
