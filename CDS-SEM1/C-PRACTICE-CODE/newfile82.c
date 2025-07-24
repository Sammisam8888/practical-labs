#include <iostream.h>
namespace ns1{
    namespace ns2{
        int m=100;
    }
};
void main()
{
    cout<<"nested namespace : \n"<<ns1::ns2::m;
    //op = 100 (since m is defined as 100 in the second nested namespace )
}