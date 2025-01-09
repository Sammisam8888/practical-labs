#include <iostream>
using namespace std;

class Fibonacci {
    int n;  // Variable to store the number of terms

public:
    void getdata();  // Function to input data
    void displayfibonnacci();  // Function to generate and display the Fibonacci series
};

// Function to input the number of terms for the Fibonacci series
void Fibonacci::getdata() {
    cout << "Enter the number of terms for the Fibonacci series: ";
    cin >> n;
}

// Function to generate and display the Fibonacci series
void Fibonacci::displayfibonnacci() {
    int a = 0, b = 1, nextTerm;

    cout << "Fibonacci Series: ";

    for (int i = 1; i <= n; i++) {
        if (i == 1) {
            cout << a << " ";
            continue;
        }
        if (i == 2) {
            cout << b << " ";
            continue;
        }
        nextTerm = a + b;
        cout << nextTerm << " ";
        a = b;
        b = nextTerm;
    }
    cout << endl;
}

int main() {
    Fibonacci fib;
    fib.getdata();
    fib.displayfibonnacci();
    return 0;
}
