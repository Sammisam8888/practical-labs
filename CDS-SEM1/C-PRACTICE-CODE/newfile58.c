#include <iostream.h>
class X{
    int a,b;
    public :
    virtual void in(){
        cout<<"Enter 2 numbers :";
        cin>>a>>b;}
        virtual void display(){
        cout<<"The numbers in class X are : "<<a<<" & "<<b;}};
class Y : public X{
    int a,b;
    public :
    void display(){
            cout<<"The numbers in class Y are : "<<a<<" & "<<b;}
    void in(){
        cout<<"Enter 2 numbers :";
        cin>>a>>b;}};      
void main()
{Y y1; cout<<"direct access through object of Y class\n";
y1.in();
y1.display(); cout<<"\n";
X *x1= new Y; 
cout<<"dynamic memory allocation through pointer object for Y class\n";
x1->in();
x1->display();
delete x1;
Y *y2= new X;
cout<<"dynamic memory allocation through pointer object for X class\n";
y2->in();
y2->display();
delete y2;
}