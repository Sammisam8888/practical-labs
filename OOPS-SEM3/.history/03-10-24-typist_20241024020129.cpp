#include <iostream>
using namespace std;

class teacher {
protected:
    string subject;
    int publication_record;
public:
    void getteacher() {
        cout << "Enter subject: ";
        cin >> subject;
        cout << "Enter publication record: ";
        cin >> publication_record;
    }
    void displayteacher() {
        cout << "Subject: " << subject << endl;
        cout << "Publication Record: " << publication_record << endl;
    }
};

class typist {
protected:
    int speed;
public:
    void gettypist() {
        cout << "Enter typing speed (words per minute): ";
        cin >> speed;
    }
    void displaytypist() {
        cout << "Typing Speed: " << speed << " wpm" << endl;
    }
};

class officer {
protected:
    char grade;
    int code_number;
public:
    void getofficer() {
        cout << "Enter officer's grade: ";
        cin >> grade;
        cout << "Enter officer's code number: ";
        cin >> code_number;
    }
    void displayofficer() {
        cout << "Officer's Grade: " << grade << endl;
        cout << "Code Number: " << code_number << endl;
    }
};

class staff : public teacher, public typist, public officer {
public:
    void getstaff() {
        getteacher();
        gettypist();
        getofficer();
    }
    void displaystaff() {
        displayteacher();
        displaytypist();
        displayofficer();
    }
};

int main() {
    staff s;
    s.getstaff();
    s.displaystaff();
    return 0;
}
