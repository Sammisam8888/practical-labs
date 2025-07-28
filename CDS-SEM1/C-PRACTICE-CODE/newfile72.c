#include <iostream.h>
class X
{int a,b;
public :
void show(void);};
void X :: show() //member function defined outside class
{a=10; b=15;
cout<<"The output is :"<<a<<" , "<<b<<endl;}
void main()
{X x1;
x1.show();} 
// op = 10 15