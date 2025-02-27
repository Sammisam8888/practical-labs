#include <iostream>
#include <ctime>
using namespace std;

class Sort
{
    int *arr, n, *temparr;
    int arrsize[4] = {5, 10, 15, 20};
    double timediff[16];
    double mintime = 1e9, maxtime = 0;
    string sortingtype[4] = {"Selection Sort ", "Insertion Sort ", "Bubble Sort ", "Heap Sort "};
    string mintype, maxtype;

    void selectionsort()
    {
        for (int i = 0; i < n; i++)
        {
            int minindex = i;
            for (int j = i; j < n; j++)
            {
                if (arr[j] < arr[minindex])
                {
                    minindex = j;
                }
            }
            swap(arr[i], arr[minindex]);
        }
    }

    void insertionsort()
    {
        for (int i = 1; i < n; i++)
        {
            int key = arr[i], j = i;
            while (j > 0 && arr[j - 1] > key)
            {
                arr[j] = arr[j - 1];
                j--;
            }
            arr[j] = key;
        }
    }

    void bubblesort()
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n - i - 1; j++)
            {
                if (arr[j] > arr[j + 1])
                {
                    swap(arr[j], arr[j + 1]);
                }
            }
        }
    }

    void heapsort()
    {
        for (int i = n / 2 - 1; i >= 0; i--)
        {
            heapify(i, n);
        }
        for (int i = n - 1; i > 0; i--)
        {
            swap(arr[0], arr[i]);
            heapify(0, i);
        }
    }

    void heapify(int i, int sz)
    {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < sz && arr[left] > arr[largest])
            largest = left;

        if (right < sz && arr[right] > arr[largest])
            largest = right;

        if (largest != i)
        {
            swap(arr[i], arr[largest]);
            heapify(largest, sz);
        }
    }

    void display(string message = "")
    {
        if (!message.empty())
        {
            cout << message << endl;
        }
        cout << "The elements of the array are: ";
        for (int i = 0; i < n; i++)
        {
            cout << arr[i] << " ";
        }
        cout << endl;
    }

    void getdata()
    {
        cout << "Enter " << n << " elements for the array : ";
        arr = new int[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
    }

    void comparetime()
    {
        cout << "The case with the minimum time: " << mintype << " took " << mintime << " seconds" << endl;
        cout << "The case with the maximum time: " << maxtype << " took " << maxtime << " seconds" << endl;
    }
    void swap(int &a, int &b)
    {
        int temp = a;
        a = b;
        b = temp;
    }
    void copyarray(int *newarr, int *oldarr)
    {

        for (int k = 0; k < n; k++)
        {
            newarr[k] = oldarr[k];
        }
    }

public:
    void runsort()
    {
        for (int i = 0; i < 4; i++)
        {

            n = arrsize[i];
            getdata();
            temparr = new int[n];
            copyarray(temparr, arr);
            mintime = 1e9, maxtime = 0;

            for (int j = 0; j < 4; j++)
            {
                int index = i * 4 + j;
                double start = double(clock()) / CLOCKS_PER_SEC;
                if (j == 0)
                {
                    selectionsort();
                }
                else if (j == 1)
                {
                    insertionsort();
                }
                else if (j == 2)
                {
                    bubblesort();
                }
                else if (j == 3)
                {
                    heapsort();
                }
                double end = double(clock()) / CLOCKS_PER_SEC;
                timediff[index] = end - start;
                cout << "For " << sortingtype[j] << endl;
                cout << "Start Time: " << start << " seconds" << endl;
                cout << "End Time: " << end << " seconds" << endl;
                cout << "Time taken: " << timediff[index] << " seconds" << endl;
                if (timediff[index] < mintime)
                {
                    mintime = timediff[index];
                    mintype = sortingtype[j];
                }
                if (timediff[index] > maxtime)
                {
                    maxtime = timediff[index];
                    maxtype = sortingtype[j];
                }
                copyarray(arr, temparr);
            }
            delete[] temparr;
            comparetime();
            delete[] arr;
        }
    }
};

int main()
{
    Sort s;
    s.runsort();
    return 0;
}
