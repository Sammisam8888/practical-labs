#include <iostream>
using namespace std;

const int INF = 1e9;

class MST {
    int **graph,*parent,*key,v;        
    bool *inMST;     

    int minKey() {
        int min = INF, min_index = -1;
        for (int i = 0; i < v; i++) {
            if (!inMST[i] && key[i] < min) {
                min = key[i];
                min_index = i;
            }
        }
        return min_index;
    }


    void display() {
        cout << "Edges in MST:\n";
        for (int i = 1; i < v; i++) {
            cout << parent[i] << " - " << i << " (Weight: " << graph[i][parent[i]] << ")\n";
        }
    }


public:
    MST() {
        cout << "Enter number of vertices: ";
        cin >> v;

        // Allocate memory dynamically
        graph = new int*[v];
        for (int i = 0; i < v; i++) {
            graph[i] = new int[v];
        }

        parent = new int[v];
        key = new int[v];
        inMST = new bool[v];

        cout << "Enter the adjacency matrix (0 if no edge):\n";
        for (int i = 0; i < v; i++) {
            for (int j = 0; j < v; j++) {
                cin >> graph[i][j];
                if (graph[i][j] == 0 && i != j)
                    graph[i][j] = INF;
            }
        }
    }
    void prim(int start = 0) {
        for (int i = 0; i < v; i++) {
            key[i] = INF;
            parent[i] = -1;
            inMST[i] = false;
        }

        key[start] = 0;

        for (int count = 0; count < v - 1; count++) {
            int u = minKey();
            inMST[u] = true;

            for (int j = 0; j < v; j++) {
                if (graph[u][j] < key[j] && !inMST[j]) {
                    parent[j] = u;
                    key[j] = graph[u][j];
                }
            }
        }

        display();
    }

    ~MST() {
        for (int i = 0; i < v; i++) {
            delete[] graph[i];
        }
        delete[] graph;
        delete[] parent;
        delete[] key;
        delete[] inMST;
    }
};

int main() {
    MST mst;
    mst.prim();
    return 0;
}
