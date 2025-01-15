#include <iostream>
using namespace std;

class Employee{
string ename,ecode;
public : 
int salary;
void getdata(){
 cout<<"Enter Employee details : "<<endl;
 cout<<"Name : ";
 cin>>ename;
 cin.ignore();
 cout<<"Employee code : ";
 cin>>ecode;
 cout<<"Enter the salary :";
 cin>>salary;
}
void displayEmp(){
 cout<<"The Employee details are : "<<endl;
 cout<<"Name :"<<ename<<endl;
 cout<<"Employee Code : "<<ecode<<endl;
 cout<<"Salary : "<<salary<<endl;
}

};
class IncomeTax : private Employee{
float taxrate,taxdeducted,netsal; 
Employee E;
public :
void gettax(){
 E.getdata();
 cout<<"Enter the Income tax details :"<<endl;
 cout<<"Tax rate(in %) : ";
 cin>>taxrate;
}
void calculateTax(){
 taxdeducted=E.salary*taxrate/100;
 netsal=E.salary-taxdeducted;
} 
void displayTax(){
 E.displayEmp();
 cout<<"The Income Tax details are : "<<endl;
 cout<<"Tax Rate : "<<taxrate<<endl;
 cout<<"Tax Deducted : "<<taxdeducted<<endl;
 cout<<"Net Salary : "<<netsal<<endl;
}
};

int main(){
IncomeTax IT;
IT.gettax();
IT.calculateTax();
IT.displayTax();
return 0;
}
