//wap to check palindrome number using class

#include <iostream>
using namespace std;    

class Solution{ 
    public:
    bool palindrome(int n){
        int rev=0,rem,m=n;
        while(n!=0){
            rem=n%10;
            rev=rev*10+rem;
            n=n/10;
        }
        return rev==m;
    }
};

int main(){
    int n;
    cout<<"Enter a number : ";
    cin>>n;
    Solution S;
    if(S.palindrome(n))
        cout<<"The number is palindrome"<<endl;
    else
        cout<<"The number is not palindrome"<<endl;
    return 0;
}