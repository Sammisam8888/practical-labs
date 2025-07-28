#include <iostream.h>
class X {
    public :
    int a;
    void f();
};
void X :: f(){
    a=20;
    cout<<a;
} 
X ob;
    
void main()
{
    ob.a=10; //here value of a is modified to 10
    ob.f(); //op = 20
}