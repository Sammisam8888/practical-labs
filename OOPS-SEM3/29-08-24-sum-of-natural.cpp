//1- wap to find sum of n natural numbers by using friend class in c++

#include <iostream>
using namespace std;
class FindSum;
class NaturalSum{
    private:
    int n,sum=0;
    public :
    NaturalSum(){
        cout<<"Enter the value of N : ";
        cin>>n;
    }
    void display(){
            cout<<"Sum of N natural odd numbers is : "<<sum<<endl;
    }
    friend class FindSum;
};
class FindSum{
    public :
int SumOfN(NaturalSum &A){
    //here it can access the private data members of the class NaturalSum
    for(int i=1;i<A.n;i+=2){
    A.sum+=i;
    cout<<i<<" + ";
    }
A.sum+=A.n;
cout<<A.n<<" = "<<A.sum<<endl;
return A.sum;
}
};
int main(){
    NaturalSum N;
    FindSum F;
    F.SumOfN(N);
    N.display();
    return 0;
}