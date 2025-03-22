#include <iostream>
#include <ctime>
using namespace std;

class Sort {
private:
    int n, *arr;
    clock_t start, end;

    void heapify(int i, int size) {
        int largest = i;
        int left = 2 * i;
        int right = 2 * i + 1;

        if (left < size && arr[left] > arr[largest])
            largest = left;

        if (right < size && arr[right] > arr[largest])
            largest = right;

        if (largest != i) {
            swap(arr[i], arr[largest]);
            heapify(largest, size);
        }
    }

    void build_max_heap() {
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(i, n);
    }

    void increase_key(int i, int key) {
        if (key < arr[i]) {
            cout << "New key is smaller than current key, operation not allowed" << endl;
            return;
        }
        arr[i] = key;
        while (i > 0 && arr[(i - 1) / 2] < arr[i]) {
            swap(arr[i], arr[(i - 1) / 2]);
            i = (i - 1) / 2;
        }
    }

    void insert_key(int key) {
        int* newArr = new int[n + 1];
        for (int i = 0; i < n; i++) newArr[i] = arr[i];
        delete[] arr;
        arr = newArr;

        arr[n] = -1; // Insert a dummy value at the last position
        n++;
        increase_key(n - 1, key);
    }

    int extract_key(int i) {
        if (n < 1) {
            cout << "Heap underflow, cannot extract key" << endl;
            return -1;
        }
        int key = arr[i];
        arr[i] = arr[n - 1];
        n--;
        if (arr[i] > arr[(i - 1) / 2]) {
            increase_key(i, arr[i]);
        } else {
            heapify(i, n);
        }
        return key;
    }

    void getdata() {
        cout << "Enter the size of the array: ";
        cin >> n;
        arr = new int[n];
        cout << "Enter the elements of the array: ";
        for (int i = 0; i < n; i++) cin >> arr[i];
    }

    void display() {
        for (int i = 0; i < n; i++) cout << arr[i] << " ";
        cout << endl;
    }
    void displaytime(clock_t start,clock_t end, string x){
        cout << "Start time: " << double(start) / CLOCKS_PER_SEC << " seconds" << endl;
        cout << "End time: " << double(end) / CLOCKS_PER_SEC << " seconds" << endl;
        cout << "Time taken to"<< x <<":"<< double(end - start) / CLOCKS_PER_SEC << " seconds" << endl;
    }
public:
    void operations() {
        getdata();
        cout << "Before building max heap: " << endl;
        display();

        start = clock();
        build_max_heap();
        end = clock();
        displaytime(start,end,"build max heap");
        cout << "After building max heap: " << endl;
        display();

        int key;
        cout << "Enter key to insert: ";
        cin >> key;
        start = clock();
        insert_key(key);
        end = clock();
        displaytime(start,end,"insert key");
        
        cout << "After inserting key: " << endl;
        display();

        cout << "Enter index to extract key: ";
        int index;
        cin >> index;
        start = clock();
        int extractedKey = extract_key(index);
        end = clock();
        cout << "Extracted key: " << extractedKey << endl;
        displaytime(start,end,"extract key");
       
        cout << "After extracting key: " << endl;
        display();

        delete[] arr;
    }
};

int main() {
    Sort s;
    s.operations();
    return 0;
}