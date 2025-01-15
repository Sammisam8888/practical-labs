#include <iostream>
#include<stack>
#include<string>
using namespace std;

class stackNode{
public :
char op;
stackNode* next;
stackNode(char x):op(x),next(nullptr){}
stackNode(char x,stackNode* nex):op(x),next(nex){}
};

class Operation{
public :
string postfix,infix;
stackNode* top=nullptr;
Operation(){
    cout<<"Enter the infix operation : ";
    getline(cin,infix);
}
void deleteNode(stackNode* top){
    if (!top) return;
    top=top->next;
}
void insertNode(char c,stackNode* top){
    stackNode* newNode=new stackNode(c,top);
    top=newNode;
}

int priority(char c){
    if (c=='^'){
        return 3;
    }
    else if (c=='*' || c=='/'){
        return 2;
    }
    else if (c=='+' || c=='-'){
        return 1;
    }
    else 
    return -1;
}
    // Function to convert an infix expression to a postfix expression.
    string infixToPostfix() {
        for (char i:infix){
            if (i==')'){
                while (top->op!='(' && top){
                    postfix.push_back(top->op);
                    deleteNode(top);
                }
                deleteNode(top); //for removing '('
            }
            else if ((i<='Z' && i>='A')||(i<='z'&&i>='a')){
                postfix.push_back(i);
            }
            else {
                while(priority(i)>priority(top->op) && top){
                postfix.push_back(top->op);
                deleteNode(top);
                }
                insertNode(i,top);
            }
            
        }
        while(top){
            postfix.push_back(top->op);
            deleteNode(top);
        }
        return postfix;
    }
};

int main(){
    Operation O;
    
    cin.ignore();
    cout<<"The postfix expression is : "<<O.infixToPostfix()<<endl;
    return 0;
}
