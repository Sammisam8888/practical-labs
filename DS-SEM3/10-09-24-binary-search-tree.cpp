#include <iostream>
using namespace std;

class TreeNode {
public:
    int value;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int v) : value(v), left(nullptr), right(nullptr) {}
};

class Tree {
private:
    TreeNode* baseroot;

    TreeNode* insertNode(TreeNode* node, int v);
    void inorder(TreeNode* node);
    void preorder(TreeNode* node);
    void postorder(TreeNode* node);

public:
    Tree() : baseroot(nullptr) {}
    void operation();  
};

TreeNode* Tree::insertNode(TreeNode* node, int v) {
    if (node == nullptr) {
        return new TreeNode(v);
    }

    if (v < node->value) {
        node->left = insertNode(node->left, v);
    } else if (v > node->value) {
        node->right = insertNode(node->right, v);
    }

    return node;
}

void Tree::inorder(TreeNode* node) {
    if (node == nullptr) return;
    inorder(node->left);
    cout << node->value << " ";
    inorder(node->right);
}

void Tree::preorder(TreeNode* node) {
    if (node == nullptr) return;
    cout << node->value << " ";
    preorder(node->left);
    preorder(node->right);
}

void Tree::postorder(TreeNode* node) {
    if (node == nullptr) return;
    postorder(node->left);
    postorder(node->right);
    cout << node->value << " ";
}


void Tree::operation() {
    int choice;
    cout << "Select Operation: 1(Insert), 2(Inorder), 3(Preorder), 4(Postorder), 5(Exit)" << endl;
    while (true) {
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                int v;
                cout << "Enter value to insert: ";
                cin >> v;
                baseroot=insertNode(baseroot,v);
                break;
            }
            case 2:
                cout << "Inorder Traversal: ";
                inorder(baseroot);
                cout<<endl;
                break;
            case 3:
                cout << "Preorder Traversal: ";
                preorder(baseroot);
                cout << endl;
                break;
            case 4:
                cout << "Postorder Traversal: ";
                postorder(baseroot);
                cout<<endl;
                break;
            case 5:
                cout << "Bye!" << endl;
                return;
            default:
                cout << "Invalid choice. Try again." << endl;
        }
    }
}

int main() {
    Tree bst;
    bst.operation();

    return 0;
}
