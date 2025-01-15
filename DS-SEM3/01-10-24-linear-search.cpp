#include <iostream>

using namespace std;

class Searching{
int n,*arr,p=-1;

public :
Searching(){
    cout<<"Enter the no of elements in the array : ";
    cin>>n;
    arr=new int[n];
    cout<<"Enter the elements of the array : "<<endl;
    for (int i=0;i<n;i++){
        cin>>arr[i];
    }
}
void linearsearch(){
    int e;
    cout<<"Enter the element to be searched : ";
    cin>>e;
    for (int i=0;i<n; i++){
        if (arr[i]==e) p=i;
    }
    if (p!=-1)
    cout<<"The element is present at index : "<<p<<endl;
    else
    cout<<"The elemet is not present in the array "<<endl;
    p=-1;
}
};

int main(){
    Searching s;
    s.linearsearch();
    return 0;
}