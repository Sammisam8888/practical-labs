#include <iostream>
using namespace std;

class MST {
    int *parent, *rank;
    int **edges;
    int **result;
    int resultCount;
    int v, e;

    void makeSet(int n) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }
    }

    int findSet(int u) {
        if (parent[u] != u)
            parent[u] = findSet(parent[u]);
        return parent[u];
    }

    void unionSets(int u, int v) {
        int uRoot = findSet(u);
        int vRoot = findSet(v);

        if (uRoot != vRoot) {
            if (rank[uRoot] < rank[vRoot])
                parent[uRoot] = vRoot;
            else if (rank[uRoot] > rank[vRoot])
                parent[vRoot] = uRoot;
            else {
                parent[vRoot] = uRoot;
                rank[uRoot]++;
            }
        }
    }

    void sortEdges() {
        for (int i = 0; i < e - 1; i++) {
            for (int j = i + 1; j < e; j++) {
                if (edges[i][2] > edges[j][2]) {
                    for (int k = 0; k < 3; k++) {
                        int temp = edges[i][k];
                        edges[i][k] = edges[j][k];
                        edges[j][k] = temp;
                    }
                }
            }
        }
    }

    void kruskal() {
        makeSet(v);
        sortEdges();
        resultCount = 0;

        for (int i = 0; i < e && resultCount < v - 1; i++) {
            int u = edges[i][0];
            int v2 = edges[i][1];
            int w = edges[i][2];

            if (findSet(u) != findSet(v2)) {
                result[resultCount][0] = u;
                result[resultCount][1] = v2;
                resultCount++;
                unionSets(u, v2);
            }
        }
    }

public:
    MST() {
        cout << "Enter number of vertices: ";
        cin >> v;
        cout << "Enter number of edges: ";
        cin >> e;

        parent = new int[v];
        rank = new int[v];

        edges = new int*[e];
        for (int i = 0; i < e; i++) {
            edges[i] = new int[3];
        }

        result = new int*[v - 1];
        for (int i = 0; i < v - 1; i++) {
            result[i] = new int[2];
        }

        cout << "Enter edges (u v w):\n";
        for (int i = 0; i < e; i++) {
            char u, v;
            int w;
            cin >> u >> v >> w;
            edges[i][0] = u - 'a';
            edges[i][1] = v - 'a';
            edges[i][2] = w;
        }
    }

    void displayMST() {
        cout << "Edges in the MST:\n";
        for (int i = 0; i < resultCount; i++) {
            cout << char(result[i][0] + 'a') << " - " << char(result[i][1] + 'a') << endl;
        }
    }

    void operations() {
        kruskal();
        displayMST();
    }

    ~MST() {
        for (int i = 0; i < e; i++) delete[] edges[i];
        delete[] edges;

        for (int i = 0; i < v - 1; i++) delete[] result[i];
        delete[] result;

        delete[] parent;
        delete[] rank;
    }
};

int main() {
    MST mst;
    mst.operations();
    return 0;
}
