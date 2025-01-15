#include <iostream>
using namespace std;

class Solution{
    public:
    int greatest(int a, int b, int c){
        if(a>b && a>c)
            return a;
        else if(b>a && b>c)
            return b;
        else
            return c;
    }
};

int main(){
    int a,b,c;
    cout<<"Enter 3 numbers : ";
    cin>>a>>b>>c;
    Solution S;
    cout<<"The greatest among the 3 numbers is : "<<S.greatest(a,b,c)<<endl;
    return 0;
}