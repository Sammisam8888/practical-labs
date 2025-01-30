#include<iostream>
#include <ctime>
using namespace std;

class Search{
int n,*arr,key,ans,pivot;
bool pivotflag=0;
string arraytypes[4] = {"Sorted Ascending", "Sorted Descending", "Unsorted", "Sorted and Unsorted mixed"};
void binarysearch(int low, int high){
    if (low>high){
        ans=-1;
        return;
    }
int mid=(high+low)/2;
if (key==arr[mid]){
ans=mid;
return;
}
else if (key<arr[mid]){
binarysearch(low,mid-1);
}
else{
binarysearch(mid+1,high);
}

}
bool checksort(){
for (int i=1;i<n;i++){
if (arr[i]>=arr[i-1]){
continue;
}
else{
return false;
}
}
return true;
}

void quicksort(int low, int high) {
        if (low >= high) return;

        if (pivotflag) {
            pivot = low;
        }

        int i = low + 1, j = high;

        while (i <= j) {
            while (i <= high && arr[i] <= arr[pivot])
                i++;
            while (j >= low && arr[j] > arr[pivot])
                j--;
            if (i < j) {
                swap(arr[i], arr[j]);
            }
        }

        pivotflag = true;
        swap(arr[pivot], arr[j]);
        quicksort(low, j - 1);
        quicksort(j + 1, high);
    }

    void display(string message = "") {
        if (!message.empty()) {
            cout << message << "\n";
        }
        cout << "The elements of the array are: ";
        for (int i = 0; i < n; i++) {
            cout << arr[i] << " ";
        }
        cout << "\n";
    }

    void getdata(string& type) {
        cout << "Enter values for a " << type << " array\nEnter the size of the array: ";
        cin >> n;
        arr = new int[n];
        cout << "Enter the elements of the array: ";
        for (int i = 0; i < n; i++){
		cin >> arr[i];
		}
		cout<<"Enter the search key : ";
		cin>>key;
    }
void displaysearchresult(){
    if (ans==-1){
        cout<<"The element "<<key<<" is not present in the array"<<endl;
    }
    else{
	cout<<"The element "<<key<<" is present at the index : "<<ans<<endl;
    }
}
	void comparetime(string minType, double minTime, string maxType, double maxTime) {
        cout << "The test with the minimum time: " << minType << " took " << minTime << " seconds"<<endl;
        cout << "The test with the maximum time: " << maxType << " took " << maxTime << " seconds"<<endl;
    }

void runsort(){
cout<<"The given array is unsorted "<<endl;
cout<<"Enter the pivot element index :";
cin>>pivot;
display("Before Sorting : ");
quicksort(0,n-1);
display("After Sorting : ");
pivotflag=0;
}

public:
void runsearch(){
double mintime=1e9,maxtime=0;
string mintype,maxtype;
for (int i=0;i<4;i++){
getdata(arraytypes[i]);

clock_t start=clock();
cout<<"Start Time : "<<double(start)/CLOCKS_PER_SEC<<"seconds"<<endl;

if (!checksort()){
runsort();
}
binarysearch(0,n-1);
clock_t end=clock();
cout<<"End Time : "<<double(end)/CLOCKS_PER_SEC<<" seconds "<<endl;
double timetaken=double(end-start)/CLOCKS_PER_SEC;
cout<<"Time taken : "<<timetaken<<" seconds"<<endl;
if (timetaken<mintime){
mintime=timetaken;
mintype=arraytypes[i];
}
if (timetaken > maxtime) {
maxtime = timetaken;
maxtype = arraytypes[i];
}
displaysearchresult();
delete[] arr;
}
comparetime(mintype,mintime,maxtype,maxtime);
}

};

int main() {
    Search s;
    s.runsearch();
    return 0;
}
