#include <iostream>
#include <string>
using namespace std;

class stackNode {
public:
    char op;
    stackNode* next;
    stackNode(char x): op(x), next(nullptr) {}
};

class Operation {
public:
    string postfix, infix;
    stackNode* top = nullptr;

    Operation() {
        cout << "Enter the infix operation: ";
        cin >> infix;
    }

    void pop() {
        if (!top) return;
        stackNode* temp = top;
        top = top->next;
        delete temp;
    }

    void push(char c) {
        stackNode* newNode = new stackNode(c);
        newNode->next = top;  // Link the new node to the existing stack
        top = newNode;        // Update the top to the new node
    }

    int priority(char c) {
        if (c == '^') {
            return 3;
        } else if (c == '*' || c == '/') {
            return 2;
        } else if (c == '+' || c == '-') {
            return 1;
        } else {
            return -1;
        }
    }

    string infixToPostfix() {
        for (char i : infix) {
            if (i == ')') {
                while (top && top->op != '(') {
                    postfix.push_back(top->op);
                    pop();
                }
                pop();  // for removing '('
            } else if ((i <= 'Z' && i >= 'A') || (i <= 'z' && i >= 'a') || (i <= '9' && i >= '0')) {
                postfix.push_back(i);
            } else if (i == '(') {
                push(i);
            } else {
                while (top && priority(i) <= priority(top->op)) {
                    postfix.push_back(top->op);
                    pop();
                }
                push(i);
            }
        }
        while (top) {
            postfix.push_back(top->op);
            pop();
        }
        return postfix;
    }
};

int main() {
    Operation O;
    cout << "The postfix expression is: " << O.infixToPostfix() << endl;
    return 0;
}
