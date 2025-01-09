#include <iostream>
using namespace std;

class QueueNode
{
public:
    int value;
    QueueNode *next;

    QueueNode(int v, QueueNode *nex) : value(v), next(nex) {}
    QueueNode(int v) : value(v), next(nullptr) {}
};

class CircularQueue
{
public:
    QueueNode *front = nullptr, *rear = nullptr;
    void display();
    void deleteQueue(); 
    void enque(int v);
    void deque();
    void operation();
};

void CircularQueue::display()
{
    if (!front) {
        cout << "Queue is empty." << endl;
        return;
    }

    QueueNode *iterator = front;
    cout << "Queue: ";
    while (iterator != rear)
    {
        cout << iterator->value << " -> ";
        iterator = iterator->next;
    }
    cout << rear->value << endl;  // Display the rear element
}

void CircularQueue::enque(int v)
{
    QueueNode *newNode = new QueueNode(v, front);
    if (!front)
    {
        front = rear = newNode;
    }
    else
    {
        rear->next = newNode;
        rear = newNode;
    }
}

void CircularQueue::deque()
{
    if (!front)
    {
        cout << "Queue is empty." << endl;
        return;
    }

    QueueNode *temp = front;
    if (front == rear)
    {
        front = rear = nullptr;
    }
    else
    {
        front = front->next;
    }
    cout << "Deleted Element is: " << temp->value << endl;
    delete temp;
}

void CircularQueue::deleteQueue()
{
    while (front)
    {
        deque();
    }
    cout << "The entire Queue was deleted." << endl;
}

void CircularQueue::operation()
{
    int choice;
    cout << "The following are the list of operations in Circular Queue: 1(Enque), 2(Deque), 3(Display), 4(Delete Queue), 5(Exit)" << endl;
    while (true)
    {
        cout << "Enter the operation to be performed: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            int v;
            cout << "Enter the element to be enqueued: ";
            cin >> v;
            enque(v);
            break;
        case 2:
            deque();
            break;
        case 3:
            display();
            break;  // Add missing break here
        case 4:
            deleteQueue();
            break;
        case 5:
            cout << "Bye!" << endl;
            exit(0);
        default:
            cout << "Invalid choice. Please try again." << endl;
        }
    }
}

int main()
{
    CircularQueue cq;
    cq.operation();
    return 0;
}
