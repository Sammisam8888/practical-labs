#include <stdio.h>
#include <stdlib.h>

// Node structure
struct Node {
    int data;
    struct Node* next;
};

// Function to search for a node with a given value
struct Node* searchNode(struct Node* head, int key) {
    struct Node* current = head;

    // Traverse the list
    while (current != NULL) {
        if (current->data == key) {
            return current;  // Node found
        }
        current = current->next;
    }

    return NULL;  // Node not found
}

// Function to print the linked list
void printList(struct Node* head) {
    struct Node* current = head;

    while (current != NULL) {
        printf("%d ", current->data);
        current = current->next;
    }

    printf("\n");
}

// Function to insert a new node at the end of the list
struct Node* insertNode(struct Node* head, int newData) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = newData;
    newNode->next = NULL;

    if (head == NULL) {
        return newNode;  // If the list is empty, the new node becomes the head
    }

    struct Node* current = head;
    while (current->next != NULL) {
        current = current->next;
    }

    current->next = newNode;  // Insert at the end
    return head;
}

// Main function
int main() {
    struct Node* head = NULL;

    // Insert nodes into the linked list
    head = insertNode(head, 1);
    insertNode(head, 2);
    insertNode(head, 3);
    insertNode(head, 4);

    printf("Linked List: ");
    printList(head);

    // Search for a node with value 3
    int keyToSearch = 3;
    struct Node* result = searchNode(head, keyToSearch);

    if (result != NULL) {
        printf("Node with value %d found.\n", keyToSearch);
    } else {
        printf("Node with value %d not found.\n", keyToSearch);
    }

    return 0;
}