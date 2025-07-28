#include <iostream.h>
class X {
    public :
    int a=10;
    int b; 
    int c=0;
    void f2();
    void f1(){
        cout<<"\na ="<<a<<" b ="<<b<<" c ="<<c; }
};
X x1; //global object

int main()
{
    X x2; //local object
    x2.b=15;
    x2.c=20; //here c is modified as 20
    cout<<"\nfor object x1 : \n";
    x1.f1(); //here b is initialised as 0 
    cout<<"\nfor object x2 : \n";
    x2.f1(); 
    cout<<"\nfor local object using f2 function\n";
   x2.f2(); 
    cout<<"\nfor global object using f2 function\n";
  x1.f2();
    return 0;
}
void X:: f2(){
    X x3; //local object
    x3.a=x3.b=5;
    x3.c=x3.a++;
    x3.f1();
}