#include <iostream>
using namespace std;

class Node {
public:
    char data;
    int freq;
    Node *left, *right;

    Node(char d, int f) {
        data = d;
        freq = f;
        left = right = NULL;
    }
};

class Huffman {
    Node **heap;
    int size;
    int n;
    char *ch;
    int *freq;
    Node *root;

    void swap(Node *&a, Node *&b) {
        Node *temp = a;
        a = b;
        b = temp;
    }

    void heapifyUp(int i) {
        while (i > 0 && heap[i]->freq < heap[(i - 1) / 2]->freq) {
            swap(heap[i], heap[(i - 1) / 2]);
            i = (i - 1) / 2;
        }
    }

    void heapifyDown(int i) {
        int smallest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;

        if (left < size && heap[left]->freq < heap[smallest]->freq)
            smallest = left;
        if (right < size && heap[right]->freq < heap[smallest]->freq)
            smallest = right;

        if (smallest != i) {
            swap(heap[i], heap[smallest]);
            heapifyDown(smallest);
        }
    }

    void insert(Node *node) {
        heap[size] = node;
        heapifyUp(size);
        size++;
    }

    Node* extractMin() {
        Node *min = heap[0];
        heap[0] = heap[--size];
        heapifyDown(0);
        return min;
    }

    void printCodes(Node *r, string code) {
        if (!r)
            return;
        if (r->left == NULL && r->right == NULL)
            cout << r->data << ": " << code << endl;
        printCodes(r->left, code + "0");
        printCodes(r->right, code + "1");
    }

public:
    Huffman() {
        size = 0;
        n = 0;
        ch = NULL;
        freq = NULL;
        heap = NULL;
        root = NULL;
        cout << "Enter number of characters: ";
        cin >> n;

        ch = new char[n];
        freq = new int[n];
        heap = new Node*[2 * n];

        cout << "Enter characters and their frequencies:\n";
        for (int i = 0; i < n; i++) {
            cin >> ch[i] >> freq[i];
            insert(new Node(ch[i], freq[i]));
        }
    }

    void operations() {
        for (int i = 1; i < n; i++) {
            Node *x = extractMin();
            Node *y = extractMin();
            Node *z = new Node('-', x->freq + y->freq);
            z->left = x;
            z->right = y;
            insert(z);
        }
        root = extractMin();
        display();
    }

    void display() {
        cout << "Huffman Codes:\n";
        printCodes(root, "");
    }

    ~Huffman() {
        delete[] ch;
        delete[] freq;
        delete[] heap;
    }
};

int main() {
    Huffman h;
    h.operations();
    return 0;
}
