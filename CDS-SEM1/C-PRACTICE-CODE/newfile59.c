#include <iostream.h>
class X{
int x;
public :
virtual void in()=0; //here it was pure virtual function 
virtual void display ()=0;};
class Y : public X{
int y;
public :
   void display(){
            cout<<"The number in class Y is : "<<y;}
    void in(){
        cout<<"Enter a number :";
        cin>>y;}};
void main()
{Y y1;
X *x1= &y1;
x1->in();
x1->display();
}