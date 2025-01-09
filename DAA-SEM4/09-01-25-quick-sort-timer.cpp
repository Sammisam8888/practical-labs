//WAP to perform quick sort operation over an array and use the clock function to print the initial and final time taken for the entire quick sort operation

#include<iostream>
using namespace std;

class Sort{
private :
int n, *arr;
void quicksort(int low, int high){

}
public :
void operations(){
cout<<"Enter the size of the array :";
cin>>n;
arr = *int [n];
cout<<"Enter the elements of the array : ";
for (int i=0;i<n;i++){
	cin>>arr[i];
}
quicksort(0,n-1)
}
};

int main(){
Sort s;
s.operations();
return 0;
}
