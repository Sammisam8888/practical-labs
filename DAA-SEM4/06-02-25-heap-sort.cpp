#include <iostream>
#include <ctime>
using namespace std;
class Sort {
    int* arr;
    int n;
    string arraytypes[4] = {"Sorted Ascending", "Sorted Descending", "Unsorted", "Sorted and Unsorted mixed"};
    double timetaken;
    void heapsort(){
         for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(i,n);
        }
        for (int i = n - 1; i > 0; i--) {
            swap(arr[0], arr[i]);  
            heapify(0, i);         
        }
    }
    void heapify(int i,int size){
        int j = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < n && arr[left] > arr[j])
            j = left;

        if (right < n && arr[right] > arr[j])
            j = right;

        if (j != i) {
            swap(arr[i], arr[size]);
            heapify(j, n);
        }
    }
	void swap(int &a, int &b){
        a+=b;
		b=a-b;
		a=a-b;
    }
    void display(string message = "") {
        if (!message.empty()) {
            cout << message << endl;
        }
        cout << "The elements of the array are: ";
        for (int i = 0; i < n; i++) {
            cout << arr[i] << " ";
        }
        cout << endl;
    }
    void getdata(string& type) {
        cout << "Enter values for a " << type << " array\nEnter the size of the array: ";
        cin >> n;
        arr = new int[n];
        cout << "Enter the elements of the array: ";
        for (int i = 0; i < n; i++) cin >> arr[i];
    }

    void runSorting(string& type) {
        getdata(type);
        display("Before sorting:");
        clock_t start = clock();
        cout << "Start time: " << double(start)/CLOCKS_PER_SEC << " seconds" << endl;
        heapsort();
        clock_t end = clock();
        cout << "End time: " << double(end)/CLOCKS_PER_SEC << " seconds" << endl;
        display("After Sorting:");
		timetaken = double(end - start) / CLOCKS_PER_SEC;
        cout << "time taken: " << timetaken << " seconds"<<endl;
        delete[] arr;
    }
    void displayResults(string mintype, double mintime, string maxtype, double maxtime) {
        cout << "The test case with the minimum time: " << mintype << " took " << mintime << " seconds"<<endl;
        cout << "The test case with the maximum time: " << maxtype << " took " << maxtime << " seconds"<<endl;
    }
public:
    void comparetime() {  
        double mintime = 1e9;
        double maxtime = 0.0;
        string mintype, maxtype;
        
        for (int i = 0; i < 4; i++) {
			runSorting(arraytypes[i]);
            if (timetaken < mintime) {
                mintime = timetaken;
                mintype = arraytypes[i];
            }
            if (timetaken > maxtime) {
                maxtime = timetaken;
                maxtype = arraytypes[i];
            }
        }
        displayResults(mintype, mintime, maxtype, maxtime);
    }
};
int main() {
    Sort s;
    s.comparetime();  
    return 0;
}
