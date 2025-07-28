#include <iostream.h>
using namespace std;
class X{
int a;
public :
void input()
{cout << "Enter a number :";
    cin>>a;}
void display ()
{cout<<"the output is :"<<a;}};
void main(){
try {
X *x1=new X();
if (x1==NULL)
cout<<"No memory allocated";
else throw x1; }
catch (X *ob){
ob->input();
ob->display();
delete ob;}}