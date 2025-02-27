#include <iostream>
#include <ctime>
using namespace std;

class Search
{
    int *arr, n, key, comp,pos;
    string arraytypes[4] = {"Sorted Ascending", "Sorted Descending", "Unsorted", "Sorted and Unsorted mixed"};
    string mintype, maxtype;
    double mintime = 1e9, maxtime = 0;
    double start, end, timetaken;
    int linearsearch(int key)
    {
        pos = -1;
        comp = 0;
        for (int i = 0; i < n; i++)
        {
            comp++;
            if (arr[i] == key)
            {
                pos = i;
                break;
            }
        }
        return pos;
    }
    void getdata(int i) {
        cout << "Enter values for a " << arraytypes[i] << " array\nEnter the size of the array: ";
        cin >> n;
        arr = new int[n];
        cout << "Enter the elements of the array: ";
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        cout << "Enter the search key: ";
        cin >> key;
    }
    void displaysearch(){
        if (pos == -1)
        {
            cout << "Element was not found in the array" << endl;
        }
        else
        {
            cout << "The given element is present at index : " << pos << endl;
        }
        cout << "The total number of comparisions : " << comp << endl;
    }
    void displaytime(){
        cout << "Start time : " << start << " seconds \n";
        cout << "End time : " << end << " seconds \n";
        cout << "Total time taken : " << timetaken << " seconds \n\n";
    }
    void comparetime(int i){
        if (timetaken < mintime) {
            mintime = timetaken;
            mintype = arraytypes[i];
        }
        if (timetaken > maxtime) {
            maxtime = timetaken;
            maxtype = arraytypes[i];
        }
    }
    void displaytimecomp()
    {
        cout << "The case with the minimum time: " << mintype << " took " << mintime << " seconds" << endl;
        cout << "The case with the maximum time: " << maxtype << " took " << maxtime << " seconds" << endl;
    }
    public:
    void runsearch()
    {   
        for (int i = 0; i < 4; i++) {
            getdata(i);
            start = double(clock()) / CLOCKS_PER_SEC;
            pos = linearsearch(key);
            end = double(clock()) / CLOCKS_PER_SEC;
            timetaken = end - start;
            displaysearch();
            displaytime();
            comparetime(i);
            delete[] arr;
        }
        displaytimecomp();
    }
};

int main()
{
    Search s;
    s.runsearch();
    return 0;
}