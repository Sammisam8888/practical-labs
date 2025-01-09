#include <iostream>
using namespace std;

class stackNode{
    public:
    int val;
    stackNode *next;
    
    stackNode(int x) : val(x), next(NULL) {}
};

class Operations{
    public :
    stackNode* top;
    int size,upperlimit;
    Operations(int sz) : top(NULL), size(0),upperlimit(sz) {}
        void push(stackNode **head, int x){
        if (size>=upperlimit) {
            cout<<"Overflow condition, please exit";
            return;
        }
        stackNode *element = new stackNode(x);
        element -> next = *head;
        *head = element;
        size++;
    }

    int pop(stackNode **head){
        if (size<=0){
            cout<<"Underflow Condition, kindly exit";
            return -1;
        }
        stackNode *temp = *head;
        *head = (*head) -> next;
        size--;
        return temp->val;
        }
};

int main(){
    int sz,x,y;
    cout<<"Enter the size of the stack : ";
    cin>>sz;
    stackNode* head=NULL;
    Operations op(sz);
    cout<<"Enter the elements of the stack : ";
    for (int i=0;i<sz;i++){
        cin>>x;
        op.push(&head,x);
    }
    cout<<"Enter the operation to be performed (1-pop,2-exit) : ";
    cin>>y;
    while(y!=2){
        cout<<"The deleted element is : "<<op.pop(&head)<<endl;
        cout<<"Enter the operation to be performed (1-pop,2-exit) : ";
        cin>>y;
    }
    cout<<endl;
    return 0;
}

