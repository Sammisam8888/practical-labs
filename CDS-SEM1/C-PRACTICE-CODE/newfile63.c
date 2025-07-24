#include <iostream.h>
using namespace std;
void main(){
int a,b; float f;
try{
cout<<"Enter two numbers : ";
cin>>a>>b;
if (b==0) throw b;
else f=(float)a/b;
throw f; }
catch (int d){
cout<<"Denominator is zero";}
catch (float f){
cout<<"The quotient is :"<<f;}
catch (...){
cout<<"Default";}}