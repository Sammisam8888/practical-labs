#include <iostream.h>
class E1
{protected :
char name[20];
int age;};
class E2 : public E1
{float h,w;
public :
void get()
{cout<<"Enter name and age :";
cin>>name>>age;
if(age<=0) throw E2();
cout<<"\nEnter height & weight :";
cin>>h>>w;}
void show ()
{cout<<"name:"<<name<<", age: "<<age<<", height :"<<h<<", weight"<<w;}};
void main()
{try{
    E2 ob;
    ob. get();
    ob. show();}
 catch (E2){
     cout<<"wrong age ";}}