#include <iostream>

using namespace std;
class Sort{
    int n,*arr;
    void heapsort(){
        for (int i=0;i<n;i++){
            heapify(i);
        }
        for (int i=0;i<int(n/2);i++){
            swap(arr[i],arr[n-1-i]);
        }
    }
    void swap(int &a, int &b){
        int temp=a;
        a=b;
        b=temp; 
    }
    void heapify(int i){
        for (int j=i;j<n;j++){
            
            if (arr[j*2+1] && arr[j]<arr[j*2+1]){
                swap(arr[j],arr[j*2+1]);
            }
            if (arr[j*2+2] && arr[j]<arr[j*2+2]){
                swap(arr[j],arr[j*2+2]);
            }
            
        }
    }
     
    void display(){
        cout <<"Elements of the array are :";
        for (int i=0;i<n;i++){
            cout <<arr[i]<<" ";
        }
        cout<<endl;
    }
    public :
    Sort(){
        cout<<"Enter number of elements :";
        cin>>n;
        cout<<"Enter the elements of the array : ";
        arr=new int[n];
        for (int i=0;i<n;i++){
            cin>>arr[i];
        }
    }
    void operations(){
        cout<<"Before sorting : "<<endl;
        display();
        heapsort();
        cout<<"After sorting :"<<endl;
        display();
    }
};

int main(){
    Sort s;
    s.operations();
    return 0;
}