//check if armstrong or not using class

#include <iostream>
#include <math.h>
using namespace std;
class armstrong{
    public:
    void checkarmstrong(int n){
        int temp = n,countdigits=0;
        int sum = 0;
        while (temp!=0) {countdigits++; temp/=10;}
        temp=n;
        while(temp != 0){
            int digit = temp % 10;
            sum += pow(sum,countdigits);
            temp /= 10;
        }
        if(sum == n){
            cout<<"The number is an armstrong number."<<endl;
        }
        else{
            cout<<"The number is not an armstrong number."<<endl;
        }
    }
};

int main(){
    int n;
    cout<<"Enter a number : ";
    cin>>n;
    armstrong a;
    a.checkarmstrong(n);
}