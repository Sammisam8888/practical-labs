#include <iostream>
using namespace std;
  
class A{
int x;
public :
void getdata(){
cout<<"Enter an integer : ";
cin>>x;
}
void display(){
cout<<"The integer is : "<<x<<endl;
}
A operator ++(){
A temp;
temp.x=++x;
return temp;
}
};

int main(){
A a1;
a1.getdata();
cout<<"Intial value : "<<endl;
a1.display();
a1=++a1;
cout<<"After increment : "<<endl;
a1.display();
return 0;
}
