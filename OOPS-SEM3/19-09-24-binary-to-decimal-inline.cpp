#include <iostream>
using namespace std;

class Operation {
    int n, binaryValue;  // Variable to store the number and binary equivalent

public:
    void getdata();
    void binaryToDecimal();  // Function to evaluate binary to decimal
    void display();          // Function to display the final output
};

// Function to input the number
void Operation::getdata() {
    cout << "Enter a number: ";
    cin >> n;
}

// Function to convert the decimal number to binary
void Operation::binaryToDecimal() {
    binaryValue = 0;
    int i = 1;  // Power of 10 (for binary digit placement)
    int temp = n;  // Keep original number intact for display

    // Convert decimal to binary
    while (temp > 0) {
        binaryValue += (temp % 2) * i;
        temp /= 2;
        i *= 10;
    }
}

// Function to display the final output
void Operation::display() {
    cout << "Binary representation of " << n << " is: " << binaryValue << endl;
}

int main() {
    Operation op;
    op.getdata();
    op.binaryToDecimal();  // Convert number to binary
    op.display();          // Display the result
    return 0;
}
