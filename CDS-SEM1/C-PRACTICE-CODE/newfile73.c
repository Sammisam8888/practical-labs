#include <iostream.h>
class X
{int a,b;
public :
void show (void);};
inline void X :: show(){ 
//inline function defined outside class
    a=10; b=15;
    cout<<a<< " & "<<b;}
void main()
{X x1;
x1. show();  //10 & 15
}