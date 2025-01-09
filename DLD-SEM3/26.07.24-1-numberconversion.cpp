//wap to convert - i - decimal to binary, ii - binary to decima

 #include <iostream>
 using namespace std;
 
 class Conversion{
 	public :
 		string decimaltobinary(int n){
 			string s="";
 			while(n>0){
 				s=char(n%2+48)+s;
 				n/=2;
 			}
 			
 			return s;
 		}
 		int binarytodecimal(string s){
 			int n=0;
 			for (int i=s.size()-1;i>=0;i--){
 				n=n*2+(s[i]-48);
 			}
 			return n;
 		}
 };
 
 int main(){
 	int n; string s;
 	cout<<"Enter a decimal number :";
 	cin>>n;
 	Conversion c;
 	cout<<"The binary value is : "<<c.decimaltobinary(n)<<endl;
 	cout<<"Enter a binary number : ";
 	cin>>s;
 	cout<<"The decimal value is : "<<c.binarytodecimal(s)<<endl;
 }
