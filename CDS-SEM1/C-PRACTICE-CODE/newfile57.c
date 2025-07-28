//hierarchical inheritance

#include <iostream.h>
#include <conio.h>
class J{
    public :
    void f(){
        cout<<"Haha\n";}
    void g(){
        cout<<"Lala\n";}};
class K : public J{
    int a,b;
    public :
    void f1(){
        cout<<"Enter 2 numbers :";
        cin>>a>>b;}
    void g1(){
        cout<<a<<" & "<<b;}};
class L : public J{
    int a,b;
    public :
    void f2(){
        cout<<"Enter 2 numbers :";
        cin>>a>>b;}
    void g2(){
        cout<<a<<" & "<<b;}};                      
                      
void main()
{clrscr();
    K p; L q;
p.f1(); p.f();
q.f2(); q.f();
cout<<"output : ";
p.g1(); p.g();
q.g2(); q.g();

}