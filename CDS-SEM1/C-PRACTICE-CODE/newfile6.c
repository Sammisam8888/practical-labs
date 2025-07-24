#include <stdio.h>
#include <stdlib.h>

// Definition for a binary tree node
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Function to create a new node
struct Node* newNode(int data) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

// Function for inorder traversal
void inorderTraversal(struct Node* root) {
    if (root != NULL) {
        // Traverse the left subtree
        inorderTraversal(root->left);

        // Visit the current node
        printf("%d ", root->data);

        // Traverse the right subtree
        inorderTraversal(root->right);
    }
}

int main() {
    // Create a sample binary tree
    struct Node* root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);

    // Perform inorder traversal
    printf("Inorder Traversal: ");
    inorderTraversal(root);

    return 0;
} 