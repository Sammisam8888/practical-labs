#include <iostream.h>
namespace n{
    int m;
    void show(){
        cout<<m;
    }
};

void main()
{
    n::m=10; //scooe resolution operator used to assign m (defined within namespace n) the value as 10 
    n:: show (); //op = 10
}