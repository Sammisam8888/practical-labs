//count digits in a nu ber using class

#include <iostream>
using namespace std;        

class Solution{
    public:
    int count(int n){
        int count=0;
        while(n!=0){
            n=n/10;
            count++;
        }
        return count;
    }
};

int main(){
    int n;
    cout<<"Enter a number : ";
    cin>>n;
    Solution S;
    cout<<"The number of digits in the number is : "<<S.count(n)<<endl;
    return 0;
}