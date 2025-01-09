#include <iostream>
using namespace std;

class Operation {
    int n;              // Variable to store the decimal number
    string binaryValue;  // Variable to store the binary equivalent

public:
    void getdata();
    inline void decimalToBinary();  // Inline function to convert decimal to binary
    void display();                 // Function to display the final output
};

// Function to input the decimal number
void Operation::getdata() {
    cout << "Enter a decimal number: ";
    cin >> n;
}

// Inline function to convert the decimal number to binary
inline void Operation::decimalToBinary() {
    binaryValue = "";   // Initialize binary value as an empty string
    int temp = n;       // Keep original number intact for display

    // Edge case: If the number is 0, binary representation is "0"
    if (temp == 0) {
        binaryValue = "0";
        return;
    }

    // Convert decimal to binary
    while (temp > 0) {
        binaryValue = (temp % 2 == 0 ? "0" : "1") + binaryValue;
        temp /= 2;
    }
}

// Function to display the final output
void Operation::display() {
    cout << "Binary representation of " << n << " is: " << binaryValue << endl;
}

int main() {
    Operation op;
    op.getdata();
    op.decimalToBinary();  // Convert number to binary
    op.display();          // Display the result
    return 0;
}
