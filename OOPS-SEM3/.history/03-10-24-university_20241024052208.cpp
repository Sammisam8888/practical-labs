#include <iostream>
using namespace std;

class student {
protected:
    string name;
public:
    void getstudent() {
        cout << "Enter student name: ";
        cin >> name;
    }
    void displaystudent() {
        cout << "Student Name: " << name << endl;
    }
};

class arts : public student {
protected:
    string university, college;
public:
    void getarts() {
        getstudent();
        cout << "Enter university name (Arts): ";
        cin >> university;
        cout << "Enter college name (Arts): ";
        cin >> college;
    }
    void displayarts() {
        displaystudent();
        cout << "University (Arts): " << university << endl;
        cout << "College (Arts): " << college << endl;
    }
};

class medical : public student {
protected:
    string university, college;
public:
    void getmedical() {
        getstudent();
        cout << "Enter university name (Medical): ";
        cin >> university;
        cout << "Enter college name (Medical): ";
        cin >> college;
    }
    void displaymedical() {
        displaystudent();
        cout << "University (Medical): " << university << endl;
        cout << "College (Medical): " << college << endl;
    }
};

class engineering : public student {
protected:
    string university, college;
public:
    void getengineering() {
        getstudent();
        cout << "Enter university name (Engineering): ";
        cin >> university;
        cout << "Enter college name (Engineering): ";
        cin >> college;
    }
    void displayengineering() {
        displaystudent();
        cout << "University (Engineering): " << university << endl;
        cout << "College (Engineering): " << college << endl;
    }
};

class cs : public engineering {
protected:
    int roll_no;
public:
    void getcs() {
        getengineering();
        cout << "Enter roll number (CS): ";
        cin >> roll_no;
    }
    void displaycs() {
        displayengineering();
        cout << "Roll No (CS): " << roll_no << endl;
    }
};

class it : public engineering {
protected:
    int roll_no;
public:
    void getit() {
        getengineering();
        cout << "Enter roll number (IT): ";
        cin >> roll_no;
    }
    void displayit() {
        displayengineering();
        cout << "Roll No (IT): " << roll_no << endl;
    }
};

class mca : public engineering {
protected:
    int roll_no;
public:
    void getmca() {
        getengineering();
        cout << "Enter roll number (MCA): ";
        cin >> roll_no;
    }
    void displaymca() {
        displayengineering();
        cout << "Roll No (MCA): " << roll_no << endl;
    }
};

void operation() {
    cs cs_student;
    it it_student;
    mca mca_student;

    cout << "Enter CS Student details:" << endl;
    cs_student.getcs();
    cout << "\nEnter IT Student details:" << endl;
    it_student.getit();
    cout << "\nEnter MCA Student details:" << endl;
    mca_student.getmca();

    cout << "\nCS Student details:" << endl;
    cs_student.displaycs();
    cout << "\nIT Student details:" << endl;
    it_student.displayit();
    cout << "\nMCA Student details:" << endl;
    mca_student.displaymca();
}

int main() {
    operation();
    return 0;
}
 