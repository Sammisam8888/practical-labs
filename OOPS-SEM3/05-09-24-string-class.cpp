//define a class string that has constructor 

#include <iostream>
using namespace std;

class String{
public:
    string s;
    String(){
        s="";
    }
    String (const string a){
        s=a;
    }

    void concat (String &a){
        s+=a.s;
    }xuu
    void display(){
        cout<<"The string object is : "<<(s==""?"Empty string":s)<<endl;
    }
};

int main(){
    String s1;
    string a="",b,c;
    s1.display();
    cout<<"Enter a string : ";
    cin>>b;
    String s2(b);
    s2.display();
    cout<<"Enter another string to be concated :";
    cin>>c;
    String s3(c);
    s2.concat(s3);
    cout<<"After concatenation : "<<endl;
    s2.display();
    return 0;
}