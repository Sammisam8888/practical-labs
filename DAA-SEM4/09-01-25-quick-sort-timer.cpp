// WAP to perform quick sort operation over an array and use the clock function to print the initial and final time taken for the entire quick sort operation

#include <iostream>
#include <ctime>
using namespace std;

class Sort
{
private:
	int n, *arr;
	void quicksort(int low, int high)
	{
		int pivot = low;

		if (low >= high)
			return;
		int i = low + 1, j = high;
		while (i <= j)
		{
			while (i <= high && arr[i] <= arr[pivot])
				i++;
			while (j >= low && arr[j] > arr[pivot])
				j--;
			if (i < j)
			{
				swap(arr[i], arr[j]);
			}
		}

		swap(arr[pivot], arr[j]);
		quicksort(low, j - 1);
		quicksort(j + 1, high);
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
	void getdata()
	{
		cout << "Enter the size of the array :";
		cin >> n;
		arr = new int[n];
		cout << "Enter the elements of the array : ";
		for (int i = 0; i < n; i++)
		{
			cin >> arr[i];
		}
	}
	void timedisplay(clock_t start, clock_t end){
		cout << "Starting time = " << double(start) / CLOCKS_PER_SEC << " seconds" << endl;
		cout << "Ending time = " << double(end) / CLOCKS_PER_SEC << " seconds" << endl;
		double time_taken = double(end - start) / CLOCKS_PER_SEC;
		cout << "Time taken for quicksort: " << time_taken << " seconds" << endl;
	}
public:
	void operations()
	{
		getdata();
		cout << "Before sorting : " << endl;
		display();
		clock_t start = clock(); // Start time

		quicksort(0, n - 1);

		clock_t end = clock(); // End time

		cout << "After Sorting : " << endl;
		display();
		timedisplay(start,end);
		delete[] arr;
	}
};

int main()
{
	Sort s;
	s.operations();
	return 0;
}
