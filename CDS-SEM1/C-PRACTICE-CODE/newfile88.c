#include <stdio.h>
#include <stdlib.h>

// Define a structure for a node
struct Node {
    int data;
    struct Node* next;
};

// Function to insert a single node at the end of the linked list
void insertAtEnd(struct Node** head, int newData) {
    // Create a new node
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = newData;
    newNode->next = NULL;

    // If the linked list is empty, make the new node the head
    if (*head == NULL) {
        *head = newNode;
    } else {
        // Traverse to the end of the linked list and insert the new node
        struct Node* last = *head;
        while (last->next != NULL) {
            last = last->next;
        }
        last->next = newNode;
    }
}

// Function to print the linked list
void printList(struct Node* node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

// Driver program
int main() {
    // Initialize an empty linked list
    struct Node* head = NULL;

    // Insert a single node at the end
    insertAtEnd(&head, 1);

    // Print the linked list
    printf("Linked List: ");
    printList(head);

    return 0;
}