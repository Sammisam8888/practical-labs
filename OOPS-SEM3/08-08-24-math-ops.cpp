#include <iostream>
using namespace std;

class Operations{
    public :
    int add(int a, int b){
        return a+b;
    }
    int sub(int a, int b){
        return a-b;
    }
    int mul(int a, int b){
        return a*b;
    }

    float div(int a, int b){
        return a/b;
    }
    float operation(int a,int b, int op){
        switch(op){
            case 1:
            return add(a,b);
            case 2:
            return sub(a,b);
            case 3:
            return mul(a,b);
            case 4:
            return div(a,b);
            default:
            cout<<"Please enter a valid operation";
            break;
        }
        
    }
};
int main(){
    int a,b,op;
    Operations O;
    cout<<"Enter 2 numbers : ";
    cin>>a>>b;
    cout<<"Enter the operation to be performed : (1-add,2-sub,3-mul,4-div,5-exit) : ";
    cin>>op;
    while(op!=5){
        cout<<"The result is : "<<O.operation(a,b,op)<<endl;
        cout<<"Enter the operation to be performed : (1-add,2-sub,3-mul,4-div,5-exit) : ";
        cin>>op;
    }
}