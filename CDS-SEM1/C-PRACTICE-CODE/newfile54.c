#include<iostream>
using namespace std;
class X{
    int x;
    public:
    void put()
    {
        x=10;
        cout<<x;
    }
};
class Y
{
int y;
public:
void put(int a)
{
    y=a;
    cout<<y;
}
};
class Z:public X,public Y
{
    
};
int main()
{
    Z z1;
    z1.put(15);
    z1.put();
   
    return 0;
}