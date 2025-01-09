#include<iostream>
using namespace std;

class Solution{
    public :
    int reverseNum(int n);
};

int Solution::reverseNum(int n){
    int rev=0;
    while(n>0){
        rev+=n%10;
        n/=10;
    }
    return rev;
}

int main(){
    int n;
    cout<<"Enter a number :";
    Solution S;
    cout<<"The reverse of the Number is : "<<S.reverseNum(n)<<endl;
    return 0;
}