#include <iostream.h>
class A{
public:
      A(){
          cout<<'a';
     }
   A(int a=0, int b=0){
 
 cout<<a<<b;
     }
 
};
void main (){
A a1;
cout<<"\n";
A a2(5);
cout<<"\n";
A a3(10,20);
}