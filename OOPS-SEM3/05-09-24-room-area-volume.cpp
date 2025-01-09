//define room class with area and volume function

#include <iostream>
using namespace std;

class room{
    public :
    int l,b,h;
    int a=0,v=0;
    room(int p,int q,int r){
        l=p;
        b=q;
        h=r;
    }
    //copy constructor
    room(room &obj){
        l=obj.l;
        b=obj.b;
        h=obj.h;
    }
    void area(){
        a=2*(l*b+l*h+b*h);
    }
    void volume(){
        v=l*b*h;
    }
    void display(){
        cout<<"The area of room is : "<<a<<endl;
        cout<<"The volume of the room is : "<<v<<endl;
    }
};

int main(){
    int l,b,h;
    cout<<"Enter length,breadth and height of the room : ";
    cin>>l>>b>>h;
    room r1(l,b,h);
    r1.area();
    r1.volume();
    cout<<"For Room 1 : "<<endl;
    r1.display();
    room r2(r1);
    r2.area(); 
    r2.volume();
    cout<<"For Room 2 : "<<endl;
    r2.display();
    room r3(r1);
    r3.area();
    r3.volume();
    cout<<"For Room 3 : "<<endl;
    r3.display();
   
    return 0;
}