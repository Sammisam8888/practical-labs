#include <iostream>
using namespace std;
class Factorial
{
int n,fact=1;
public:
    void getdata(){
        cout<<"Enter the number : ";
        cin>>n;
    }
    void display(){
        cout<<"Factorial of the number : "<<facto(n)<<endl;
    }
    int facto(int n)
    {
        if (n == 0)
        {
            return 1;
        }
        else
        {
            return n * facto(n - 1);
        }
    }
};

int main()
{
 Factorial f;
 f.getdata();
 f.display();
 return 0;
}