#include <iostream>
using namespace std;

class CubeSum{
    private:
    int n,sum=0;
    public :
    CubeSum(){
        cout<<"Enter the value of N : ";
        cin>>n;
    }
    void display(){
        cout<<"Sum of N natural numbers is : "<<sum<<endl;
    }
    friend int SumOfCube(CubeSum &A);

};

int SumOfCube(CubeSum &A){
    //here it can access the private data members of the class CubeSum
    for(int i=1;i<A.n;i++){
    A.sum+=(i*i*i);
    cout<<i<<"^3 + ";
    }
    A.sum+=(A.n*A.n*A.n);
    cout<<A.n<<"^3 = "<<A.sum<<endl;
    return A.sum;
}

int main(){
    CubeSum C;
    SumOfCube(C);
    C.display();
    return 0;
}