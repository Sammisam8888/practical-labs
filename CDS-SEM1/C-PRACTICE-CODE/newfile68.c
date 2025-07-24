#include <iostream.h>
using namespace std;
void divide (int x,int y)
{if(y==0)
throw "exception caught";
else cout<<(x/y);}
void main()
{int m,n;
cout<<"Enter two numbers :";
cin>>n>>m;
try
{try{
    divide(n,m);}
 catch(const char *m)
 {cout<<endl<<m<<" this is inner catch block\n";
     throw;}}
catch (const char *rem)
{cout<<rem<<" this is the outer catch block";}}