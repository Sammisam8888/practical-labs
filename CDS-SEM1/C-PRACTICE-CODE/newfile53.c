#include <iostream.h>
class X{
    int a[5];
    public :
    void operator [](int i){
        cin>>a[i];
        cout<<a[i];}};
void main()
{X x1;
cout<<"Enter 5 numbers :";
int i;
for (i=0;i<5;i++){
    cout <<"\nEnter the "<<i+1<<"th number :";
    x1[i];}}