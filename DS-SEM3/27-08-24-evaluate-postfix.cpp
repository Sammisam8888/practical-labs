#include <iostream>
#include <math.h>
using namespace std;

class stackNode{
public:
double x;
stackNode *next;

stackNode(double val,stackNode* nex):x(val),next(nex){}
};

class Evaluation{
public :
string postfix;
double result=0;
stackNode* top=nullptr;
Evaluation(){
cout<<"Enter the postfix expression : ";
getline(cin,postfix);
}
double operation(char op, double a, double b){
switch(op){
case '+':
return a+b;
case '-':
return a-b;
case '*':
return a*b;
case '/':
return (double)a/b;
case '^':
return pow(a,b);

}
return 0;
}

double EvaluatePostfix(){
for (int i=0;i<postfix.size();i++){
if (postfix[i]==' ') continue;
else if (postfix[i]>='0' && postfix[i]<='9'){
	stackNode* newNode=new stackNode ((int)(postfix[i]-'0'),top);
	top=newNode;
}
else{
	double b=top->x; 
	top=top->next; //pop operation in stack to remove the most recent element;
	result=operation(postfix[i],top->x,b);
	top=top->next; // to remove the second element;
	stackNode* newNode = new stackNode(result,top);
	top=newNode; //new updated result is pushed
}
}
return result;
}
};
int main(){
Evaluation E;
cout<<"The value of the postfix expression is : "<<E.EvaluatePostfix()<<endl;
return 0;
}
