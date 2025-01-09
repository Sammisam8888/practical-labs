//wap to overload on binary + operator for complex number addition

#include <iostream>
using namespace std;

class A{
int a,b,asum,bsum;
public :
void getdata(){
cout<<"Enter the coefficient of real and imaginary part of complex number : ";
cin>>a>>b;
}
void display(){
cout<<"The Complex number is : "<<a<<" + "<<b<<"i"<<endl;
}
void displaySum(){
cout<<"The sum of the complex numbers is : "<<asum<<" + "<<bsum<<"i"<<endl;
}
A operator +(A &obj){
A temp;
temp.asum=a+obj.a;
temp.bsum=b+obj.b;
return temp;
}
};

int main(){
A c1,c2,c3;
cout<<"For complex no 1 : "<<endl;
c1.getdata();
c1.display();
cout<<"For complex no 2 : "<<endl;
c2.getdata();
c2.display();
c3=c1+c2;
c3.displaySum();
return 0;
}
