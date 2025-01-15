//wap to take 50 numbers in an array and display all even number followed by odd numbers 

#include <iostream>
using namespace std;

class Operation{
int arr[50];
public:
void getdata();
void display();
};
void Operation::getdata(){
cout<<"Enter 50 elements of the array : "<<endl;
for (int i=0;i<50;i++){
  cin>>arr[i];
 }
}
void Operation::display(){
 cout<<"Even elements are : "<<endl;
 for (int i=0;i<50;i++) {
 if (!(arr[i]%2)) cout<<arr[i]<<" ";
 }
 cout<<endl<<"Odd elements are : "<<endl;
 for (int i=0;i<50;i++) {
 if (arr[i]%2) cout<<arr[i]<<" ";
 }
 }

int main(){
Operation obj;
obj.getdata();
obj.display();
return 0;
}
 
