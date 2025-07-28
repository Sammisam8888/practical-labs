#include <iostream.h>
class X{
int a;
public : 
X(int i){
a=i;}
operator int(){
return a; }
operator float(){
return a;}};
void main (){
X h(20);
int y=h;
float z=h;
cout<<y; // op=20
cout<<"float : "<<z; } // op=20.0
