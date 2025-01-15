#include <iostream>
using namespace std;

class Editor{
public :
 string ename,ecode, doj;
void getdata(){
 cout<<"Enter the employee details : "<<endl;
 cout<<"Name : ";
 cin>>ename;
 cin.ignore();
 cout<<"Employee code : ";
 cin>>ecode;
 cout<<"Date of joining : ";
 cin>>doj;
}
void displayEmp(){
 cout<<"The employee details are :"<<endl;
 cout<<"Name : "<<ename<<endl;
 cout<<"Employee Code : "<<ecode<<endl;
 cout<<"Date of Joining : "<<doj<<endl;
}
};
class Reporter : public Editor{
 string field_of_op;
 int years_of_exp;
public :
void getreport(){
 cout<<"Enter Reported details : "<<endl;
 cout<<"Field of operation : ";
 cin>>field_of_op;
 cout<<"Years of experience : ";
 cin>>years_of_exp;
}
void displayReporter(){
 cout<<"The reported details are : "<<endl;
 cout<<"Field of operation is : "<<field_of_op<<endl;
 cout<<"Years of experience is : "<<years_of_exp<<endl;
}
};	
int main(){
Reporter Ed;
Ed.getdata();
Ed.getreport();
Ed.displayEmp();
Ed.displayReporter();
return 0;
}
