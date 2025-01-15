/*
1. Define a class employee with the following specificaions :
empno - int
ename - string
basic,hra,da - float
netpay - float
member functions :
calculate () - a function to calculate basic+hra+da with float return type
getdata()- a func to take input of empno, ename, basic, hra, da & involve calculate method to find netpay
display() - function to display all data members
*/

#include <iostream>
using namespace std;

class Employee{
    int empno;
    string ename;
    float hra,da,basic,netpay;
    public :
    void getdata();
    void display();
    float calculate();
};

void Employee::getdata(){
    cout<<"Enter the employee details : "<<endl;
    cout<<"Enter Employee No. : ";
    cin>>empno;
    cout<<"Enter Employee name : ";
    cin.ignore();
    getline(cin,ename);
    cout<<"Enter the basic pay : ";
    cin>>basic;
    cout<<"Enter the HRA : ";
    cin>>hra;
    cout<<"Enter the DA : ";
    cin>>da;
    netpay=calculate();
}

float Employee::calculate(){
    return basic+hra+da; 
}

void Employee::display(){
    cout<<"The Employee details are : "<<endl;
    cout<<"The Employee No is : "<<empno<<endl;
    cout<<"The Employee name is : "<<ename<<endl;
    cout<<"The Employee's Basic Pay is : "<<basic<<endl;
    cout<<"The Employee's HRA is : "<<hra<<endl;
    cout<<"The Employee's DA is : "<<da<<endl;
    cout<<"The Employee's NETPAY is : "<<netpay<<endl;
}

int main(){
    Employee E;
    E.getdata();
    E.display();
    return 0;
}
