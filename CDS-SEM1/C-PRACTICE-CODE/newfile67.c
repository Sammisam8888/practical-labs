#include<iostream>
using namespace std;
int main()
{   int a,b;
    float f;
    try
    { cout<<"enter two nos: \n";
        cin>>a>>b;
        if(b==0)
        throw b;
        else 
        f=(float)a/b;
        throw f;   }
    //catch(int d)
    //{
    //    cout<<"Denominator is zero ";
   // }
    catch(float f)
    {cout<<"result= "<<f;    }
    catch(...)
    {   cout<<"default";    }
    return 0;}