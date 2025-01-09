//display factors of a number using class

#include <iostream>
using namespace std;
class factors{
    public:
    void displayfactors(int n){
        cout<<"The factors of the number are : "<<endl;
        for(int i=1;i<=n;i++){
            if(n%i==0){
                cout<<i<<endl;
            }
        }
    }
};

int main(){
    int n;
    cout<<"Enter a number : ";
    cin>>n;
    factors f;
    f.displayfactors(n);
}