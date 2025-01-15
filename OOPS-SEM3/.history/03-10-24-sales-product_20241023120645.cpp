#include <iostream>
using namespace std;

class sales{
    protected:
    string salesman;
    int qtysold,salary;
    public:
    void getsales(){
        cout<<"Enter salesman : ";
        cin>>salesman;
        cout<<"Enter quantity sold : ";
        cin>>qtysold;
        cout<<"Enter salary : ";
        cin>>salary;
    }
    void displaysales(){
        cout<<"Salesman : "<<salesman<<endl;
        cout<<"Quantity sold : "<<qtysold<<endl;
        cout<<"Salary : "<<salary<<endl;
    }
};
class commission : protected sales {
    float commrate,totalsal,commearned;
    
};