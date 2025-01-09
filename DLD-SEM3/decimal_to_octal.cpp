#include<iostream>
#include<math.h>
using namespace std;
void D_O(long long num){
	string t = "";
	while(num){
		int r = num%8;
		t = (char)(r+'0')+t;
		num/=8;
	}
	cout <<"Octal Number is : "<<t;
}
void O_D(long long num)
{
	long long d=0,cnt = 0;
	while(num)
	{
		d+=(pow(8,cnt)*(num%10));
		num/=10;
		cnt++;
	}
	cout<<"Decimsl Number is:"<<d;
}
void H_D(long long num){
	long long s = 0,cnt = 0;
	while(num){
		s+=(16)
	}
}
int main () {
	D_O(80);
	cout<<endl;
	O_D(120);
}
