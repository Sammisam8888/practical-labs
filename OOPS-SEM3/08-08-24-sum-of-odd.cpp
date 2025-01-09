#include <iostream>
using namespace std;

class Solution{
    public :
    int sumOfodd(){
        int sum=0;
        for(int i=1;i<100;i+=2)
            sum+=i;
        return sum;
    }
};

int main (){
    Solution S;
    cout<<"Sum of odd numbers from 1 to 100 is : "<<S.sumOfodd();
    return 0;
}