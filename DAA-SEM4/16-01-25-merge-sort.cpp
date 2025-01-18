#include <iostream>
#include <ctime>
#include <string>
#include <climits>
using namespace std;

class Sort{
private :
int n,*arr;
double timediff[12];
string type [4]= {"Sorted Ascending array","Sorted Descending Array","Unsorted array", "Sorted and Unsorted mixed array"};
    void mergesort(int low, int high) {
        if (low >= high) {
            return;
        }

        int mid = low + (high - low) / 2;

        // Recursive sorting of the left and right halves
        mergesort(low, mid);
        mergesort(mid + 1, high);

        // Merge the sorted halves
        merge(low, mid, high);
    }

    void merge(int low, int mid, int high) {
        int leftSize = mid - low + 1;
        int rightSize = high - mid;

        // Temporary arrays for left and right halves
        int* left = new int[leftSize];
        int* right = new int[rightSize];

        for (int i = 0; i < leftSize; i++) {
            left[i] = arr[low + i];
        }
        for (int i = 0; i < rightSize; i++) {
            right[i] = arr[mid + 1 + i];
        }

        int i = 0, j = 0, k = low;

        // Merge the arrays back into the main array
        while (i < leftSize && j < rightSize) {
            if (left[i] <= right[j]) {
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }

        // Copy remaining elements, if any
        while (i < leftSize) {
            arr[k++] = left[i++];
        }
        while (j < rightSize) {
            arr[k++] = right[j++];
        }

        delete[] left;
        delete[] right;
    }
void display()
	{
		cout << "The elements of the array are : " << endl;
		for (int i = 0; i < n; i++)
		{
			cout << arr[i] << " ";
		}
		cout << endl;
	}
	void getdata(int c)
	{	cout<<"Enter values for a "<<type[c]<<endl;
		cout << "Enter the size of the array :";
		cin >> n;
		arr = new int[n];
		cout << "Enter the elements of the array : ";
		for (int i = 0; i < n; i++)
		{
			cin >> arr[i];
		}

	}
	void calculatetime(clock_t start, clock_t end, int i){
		timediff[i*3]=double(start) / CLOCKS_PER_SEC;
		timediff[i*3+1]=double(end) / CLOCKS_PER_SEC;
		timediff[i*3+2] = double(end - start) / CLOCKS_PER_SEC;		
	}
	void displaytimediff() {
    int slow = 0, fast = 0; // Indices for slowest and fastest types
    cout << "The time differences between the 4 types of sorting are as follows:" << endl;

    for (int i = 0; i < 4; i++) {
        cout << "For " << type[i] << ":" << endl;
        cout << "Initial time: " << timediff[i * 3] << " seconds" << endl;
        cout << "Final time: " << timediff[i * 3 + 1] << " seconds" << endl;
        cout << "Time taken: " << timediff[i * 3 + 2] << " seconds" << endl;

        // Update indices for the fastest and slowest types
        if (timediff[i * 3 + 2] < timediff[fast * 3 + 2]) {
            fast = i;
        }
        if (timediff[i * 3 + 2] > timediff[slow * 3 + 2]) {
            slow = i;
        }
    }

    // Output the fastest and slowest cases
    cout << "According to the above comparison of time differences, " << type[fast]
         << " is taking the least time to perform merge sort, with a complexity of "
         << timediff[fast * 3 + 2] << " seconds." << endl;

    cout << "And " << type[slow]
         << " is taking the most time compared to others, with a complexity of "
         << timediff[slow * 3 + 2] << " seconds." << endl;
}

public:
	void operations()
	{

	for (int i=0;i<4;i++){
		getdata(i);
		cout << "Before sorting : " << endl;
		display();

		clock_t start = clock(); // Start time

		mergesort(0, n - 1);

		clock_t end = clock(); // End time

		cout << "After Sorting : " << endl;
		display();

		calculatetime(start,end,i);

		delete[] arr;
		}
	displaytimediff();
	}
};

int main()
{
	Sort s;
	s.operations();
	return 0;
}



