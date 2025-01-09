//wap to find the most frequent element in the array

#include <iostream>
#include <map>
using namespace std;

class Operation{
 int n,*arr,maxfreq;
 map<int,int> counter;
 public:
  void getdata();
  void display();
  void countfrequency();
};

void Operation::getdata(){
 cout<<"Enter the size of the array : ";
 cin>>n;
 arr=new int[n];
 cout<<"Enter the elements in the array : "<<endl;
 for (int i=0;i<n;i++){
  cin>>arr[i];
 }
}
void Operation::countfrequency(){
 for (int i=0;i<n;i++){
  counter[arr[i]]++;
 }
 int maxcount=0;
 maxfreq=arr[0];
 for (const auto &i : counter){
 if (i.second>maxcount) { maxfreq=i.first;maxcount=i.second;}
 }
 
}
void Operation::display(){
 cout<<"The most frequent element in the array is : "<<maxfreq<<endl;
}



int main(){
Operation op;
op.getdata();
op.countfrequency();
op.display();
return 0;
}
