#include <iostream>
using namespace std;
class QueueNode{
    public :
    int v;
    QueueNode* next, *prev;
    QueueNode(int v) : v(v), next(nullptr), prev(nullptr) {}
    QueueNode(int v, QueueNode* next, QueueNode* prev) : v(v), next(next), prev(prev) {}
};
class LinearQueue{
    public :
    QueueNode *front=nullptr,*rear=nullptr;
    void display();
    void enque(int v);
    void deque();
    bool isempty();
    void operation();
};
void LinearQueue::display(){
    QueueNode* temp=front;
    while(temp){
        cout<<temp->v;
        if(temp->next) cout<<"->";
        temp=temp->next;
    }
    cout<<endl;
}
void LinearQueue::enque(int v){
    QueueNode* temp=new QueueNode(v);
    if(!front){
        front=rear=temp;
    }
    else{
        rear->next=temp;
        temp->prev=rear;
        rear=temp;
    }
}
void LinearQueue::deque(){
    QueueNode* temp=front;
    if(!front){
        cout<<"Queue is empty"<<endl;
        return;
    }
    if(front==rear){
        front=rear=nullptr;
    }
    else{
        front=front->next;
        front->prev=nullptr;
    }
    cout<<"Deleted Element is : "<<temp->v<<endl;
    delete temp;
}

bool LinearQueue::isempty(){
    return (!front);
}

void LinearQueue::operation(){
    cout<<"The following are the list of operations : 1(Enqueue) 2(Dequeue) 3(Display) 4(Exit)"<<endl;
    cout<<"Enter the operation to be performed :";
    int choice;
    cin>>choice;
    while(choice!=4){
        switch(choice){
            case 1:
            int v;
            cout<<"Enter the value to be enqueued :";
            cin>>v;
            enque(v);
            break;
            case 2:
            deque();
            break;
            case 3:
            display();
            break;
            default:
            cout<<"Please enter a valid operation :"<<endl;
            break;
        }
        cout<<"Enter the operation to be performed :";
        cin>>choice;
    }
    cout<<"Bye!"<<endl;
}
int main(){
    LinearQueue q;
    q.operation();
    return 0;
}