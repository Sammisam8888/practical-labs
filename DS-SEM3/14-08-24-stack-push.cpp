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
};

int main(){
    int sz,x,y;
    cout<<"Enter the size of the stack : ";
    cin>>sz;
    stackNode* head=NULL;
    Operations op(sz);
    cout<<"Enter the operation to be performed (1-push,2-exit) : ";
    cin>>y;
    while(y!=2){
        cout<<"Enter the element to be inserted : ";
        cin>>x;
        op.push(&head,x);
        cout<<"Enter the operation to be performed (1-push,2-exit) : ";
        cin>>y;
    }
    cout<<endl;
    return 0;
}

