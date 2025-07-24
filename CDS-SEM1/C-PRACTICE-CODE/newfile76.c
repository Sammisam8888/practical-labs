#include <iostream.h>
class X
{int a;
private :
X(){
    a=10;
    cout<<"constructor called \n";}
~X(){
    cout<<"Destructor called \n";}
public :
void show (){
    this ->X::X();
    cout<<"a = "<<a;
    this->X::~X();}};
        
int main()
{X *x1;
x1->show();
return 0;}