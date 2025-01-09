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
    TreeNode* p = nullptr;

    TreeNode* insertNode(TreeNode* node, int v);
    void inorder(TreeNode* node);
    void preorder(TreeNode* node);
    void postorder(TreeNode* node);
    TreeNode* searchNode(TreeNode* node, TreeNode* parent, int v);
    TreeNode* deleteElement(TreeNode* node, int v);
    TreeNode* findMin(TreeNode* node);

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

TreeNode* Tree::searchNode(TreeNode* node, TreeNode* parent, int v) {
    if (!node || node->value == v) {
        p = parent;
        return node;
    }

    if (v < node->value) {
        return searchNode(node->left, node, v);
    } else {
        return searchNode(node->right, node, v);
    }
}

TreeNode* Tree::findMin(TreeNode* node) {
    while (node->left) {
        node = node->left;
    }
    return node;
}

TreeNode* Tree::deleteElement(TreeNode* node, int v) {
    if (!node) {
        return node;
    }

    if (v < node->value) {
        node->left = deleteElement(node->left, v);
    } else if (v > node->value) {
        node->right = deleteElement(node->right, v);
    } else {
        // Node to be deleted found
        if (node->left == nullptr && node->right == nullptr) {
            delete node;
            return nullptr;
        } else if (!node->left) {
            TreeNode* temp = node->right;
            delete node;
            return temp;
        } else if (!node->right) {
            TreeNode* temp = node->left;
            delete node;
            return temp;
        } else {
            TreeNode* temp = findMin(node->right);
            node->value = temp->value;
            node->right = deleteElement(node->right, temp->value);
        }
    }
    return node;
}

void Tree::inorder(TreeNode* node) {
    if (!node) return;
    inorder(node->left);
    cout << node->value << " ";
    inorder(node->right);
}

void Tree::preorder(TreeNode* node) {
    if (!node) return;
    cout << node->value << " ";
    preorder(node->left);
    preorder(node->right);
}

void Tree::postorder(TreeNode* node) {
    if (!node) return;
    postorder(node->left);
    postorder(node->right);
    cout << node->value << " ";
}

void Tree::operation() {
    int choice;
    cout << "Select Operation for Binary Search Tree : 1(Insert), 2(Inorder), 3(Preorder), 4(Postorder), 5(Search), 6(Delete), 7(Exit)" << endl;
    while (true) {
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                int v;
                cout << "Enter an element : ";
                cin >> v;
                baseroot = insertNode(baseroot, v);
                break;
            }
            case 2:
                cout << "Inorder Traversal: ";
                inorder(baseroot);
                cout << endl;
                break;
            case 3:
                cout << "Preorder Traversal: ";
                preorder(baseroot);
                cout << endl;
                break;
            case 4:
                cout << "Postorder Traversal: ";
                postorder(baseroot);
                cout << endl;
                break;
            case 5: {
                int v;
                cout << "Enter the element to be searched: ";
                cin >> v;
                TreeNode* result = searchNode(baseroot, nullptr, v);
                if (result) {
                    cout << "Element found: " << result->value << endl;
                    if (p) {
                        cout << "The parent Node is: " << p->value << endl;
                        p=nullptr;                        
                    } else {
                        cout << "The given value is present at the root node" << endl;
                    }
                } else {
                    cout << "Element not found" << endl;
                }
                break;
            }
            case 6: {
                int v;
                cout << "Enter value to delete: ";
                cin >> v;
                baseroot = deleteElement(baseroot, v);
                break;
            }
            case 7:
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

