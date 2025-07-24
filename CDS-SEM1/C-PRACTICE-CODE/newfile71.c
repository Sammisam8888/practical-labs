#include <iostream.h>
class X{};
class Y{};
void main()
{try{
    //cout<<"uncaught exception ";
    throw X();}
    catch(X)
    {cout<<"Exception for X";}
}