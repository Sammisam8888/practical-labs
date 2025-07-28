#include <iostream.h>
using namespace std;
void main()
{int x,y;
try{
cout<<"Enter two values :";
cin>>x>>y;
if (x==0){
throw "x is zero";}
if (y==0) throw y;
if(x<0)
throw "x is negative";
cout<<x/y; }
catch (int k){
cout<<"The throw value is :"<<k;}
catch (const char *m){
cout<<m;}};