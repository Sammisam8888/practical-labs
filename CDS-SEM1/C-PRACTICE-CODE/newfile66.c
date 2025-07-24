#include <iostream.h>
using namespace std;
void fun(int p,float q) throw (int, float)
{if (p==0) throw p;
if (q==0.0) throw q;}    
int main()
{int x; float y;
cin>>x>>y;
try
{fun(x,y);}
catch(int x)
{cout<<"Exception for int :"<<x;}
catch(float y)
{cout<<"Exception for float : "<<y;}
return 0;}