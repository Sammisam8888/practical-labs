#include <iostream>
using namespace std;

class StackNode {
public:
    int data;
    StackNode *next;
    StackNode(int value) : data(value), next(nullptr) {}
};

class Stack {
    StackNode *top;

public:
    Stack() : top(nullptr) {}

    bool isEmpty() {
        return top == nullptr;
    }

    void push(int value) {
        StackNode *newNode = new StackNode(value);
        newNode->next = top;
        top = newNode;
    }

    int pop() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        int value = top->data;
        StackNode *temp = top;
        top = top->next;
        delete temp;
        return value;
    }
};

class Graph {
    int n, m,**adj,*visited;

public:
    int start;
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

        cout << "Enter the starting node for DFS traversal: ";
        cin >> start;
    }

    void dfs(int node) {
        Stack s;
        s.push(node);
        visited[node] = 1;

        cout << "DFS Traversal: ";

        while (!s.isEmpty()) {
            int curr = s.pop();
            cout << curr << " ";

            for (int i = 0; i < n; i++) {
                if (adj[curr][i] == 1 && !visited[i]) {
                    visited[i] = 1;
                    s.push(i);
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
    g.dfs(g.start); // Start DFS from the initialized starting node
    return 0;
}