#include <iostream>
using namespace std;

class student {
protected:
    int roll_no;
public:
    void getstudent() {
        cout << "Enter Roll No: ";
        cin >> roll_no;
    }
    void displaystudent() {
        cout << "Roll No: " << roll_no << endl;
    }
};

class test : public student {
protected:
    int marks1, marks2;
public:
    void gettest() {
        getstudent();
        cout << "Enter marks for subject 1: ";
        cin >> marks1;
        cout << "Enter marks for subject 2: ";
        cin >> marks2;
    }
    void displaytest() {
        displaystudent();
        cout << "Marks in subject 1: " << marks1 << endl;
        cout << "Marks in subject 2: " << marks2 << endl;
    }
};

class result : public test {
    int total_marks;
public:
    void getresult() {
        gettest();
        total_marks = marks1 + marks2;
    }
    void displayresult() {
        displaytest();
        cout << "Total Marks: " << total_marks << endl;
    }
};

int main() {
    result r;
    r.getresult();
    r.displayresult();
    return 0;
}
