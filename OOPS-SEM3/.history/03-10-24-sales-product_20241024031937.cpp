#include <iostream>
using namespace std;

class sales {
protected:
    string salesman;
    int qtysold, salary;
public:
    void getsales() {
        cout << "Enter salesman name : ";
        cin >> salesman;
        cout << "Enter quantity sold: ";
        cin >> qtysold;
        cout << "Enter salary: ";
        cin >> salary;
    }
    void displaysales() {
        cout << "Salesman name : " << salesman << endl;
        cout << "Quantity sold: " << qtysold << endl;
        cout << "Salary: " << salary << endl;
    }
};

class commission : protected sales {
    float commrate, totalsal, commearned;
public:
    void getcommission() {
        getsales();
        cout << "Enter commission rate (%): ";
        cin >> commrate;
    }
        commearned = (commrate / 100) * qtysold;
        totalsal = salary + commearned;
    }
    void displaycommission() {
        displaysales();
        cout << "Commission rate: " << commrate << "%" << endl;
        cout << "Commission earned: " << commearned << endl;
        cout << "Total salary: " << totalsal << endl;
    }
};

int main() {
    commission c;
    c.getcommission();
    c.displaycommission();
    return 0;
}
