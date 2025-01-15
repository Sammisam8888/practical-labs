#include <iostream>
using namespace std;

class QueueNode {
public:
    int data;
    QueueNode *next;
    QueueNode(int value) : data(value), next(nullptr) {}
};

class Queue {
    QueueNode *front, *rear;

public:
    Queue() : front(nullptr), rear(nullptr) {}

    bool isEmpty() {
        return front == nullptr;
    }

    void enqueue(int value) {
        QueueNode *newNode = new QueueNode(value);
        if (rear == nullptr) {
            front = rear = newNode;
            return;
        }
        rear->next = newNode;
        rear = newNode;
    }

    int dequeue() {
        if (isEmpty()) {
            cout << "Queue is empty!" << endl;
            return -1;
        }
        int value = front->data;
        QueueNode *temp = front;
        front = front->next;
        if (front == nullptr)
            rear = nullptr;
        delete temp;
        return value;
    }
};

class Graph {
    int n, m, start;
    int **adj;
    int *visited;

public:
    // Default constructor to initialize the graph
    Graph() {
        cout << "Enter the number of nodes: ";
        cin >> n;
        cout << "Enter the number of edges: ";
        cin >> m;

        adj = new int*[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new int[n]();
        }

        visited = new int[n]();

        cout << "Enter the edges (u v):" << endl;
        for (int i = 0; i < m; i++) {
            int u, v;
            cin >> u >> v;
            adj[u][v] = 1;
            adj[v][u] = 1; // For undirected graph
        }

        cout << "Enter the starting node for BFS traversal: ";
        cin >> start;
    }

    void bfs() {
        Queue q;
        q.enqueue(start);
        visited[start] = 1;
        cout << "BFS Traversal: ";

        while (!q.isEmpty()) {
            int node = q.dequeue();
            cout << node << " ";
            
            for (int i = 0; i < n; i++) {
                if (adj[node][i] == 1 && !visited[i]) {
                    visited[i] = 1;
                    q.enqueue(i);
                }
            }
        }
        cout << endl;
    }

    ~Graph() {
        for (int i = 0; i < n; i++) {
            delete[] adj[i];
        }
        delete[] adj;
        delete[] visited;
    }
};

int main() {
    Graph g;
    g.bfs();
    return 0;
}