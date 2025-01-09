//3- wap to demonstrate the use of friend function to add private data of two different class

#include <iostream>
using namespace std;
class B;
class A{
    private :
    int a;
    public :
    A(){
        cout<<"Enter the value of A : ";
        cin>>a;
    }
    friend int Add(A &A1, B &B1);
};
class B{
    int b;
    public:
    B(){
        cout<<"Enter the value of B : ";
        cin>>b;
    }
    friend int Add(A &A1, B &B1);
};

int Add(A &A1, B &B1){
    return A1.a+B1.b;
}

int main(){
    A A1;
    B B1;
    cout<<"The sum of A and B is : "<<Add(A1,B1)<<endl;
    return 0;
}