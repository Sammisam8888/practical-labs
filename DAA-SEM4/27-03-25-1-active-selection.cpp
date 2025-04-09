#include <iostream>
using namespace std;

class Selection {
    int n;
    int *s, *f, *counter;
    int *selectedjobs;
    int sc = 0;

    void recursiveActivitySelection(int i, int j) {
        int m = i + 1;
        while (m < j && s[m] < f[i]) {
            m++;
        }
        if (m < j) {
            selectedjobs[sc++] = counter[m] + 1; // counter[m] used to retain the original job number
            recursiveActivitySelection(m, j);
        }
    }

    void sortft() {
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (f[i] > f[j]) {
                    swap(f[i],f[j]);
                    swap(counter[i],counter[j]);
                    swap(s[i],s[j]);
                }
            }
        }
    }
    void swap(int &a,int &b){
        int temp =a;
        a=b;
        b=temp;
    }

public:
    Selection() {
        cout << "Enter the number of activities: ";
        cin >> n;
        selectedjobs = new int[n];
        s = new int[n];
        f = new int[n]; 
        counter=new int [n];
        cout << "Enter start times: ";
        for (int i = 0; i < n; i++) {
            counter[i]=i;
            cin >> s[i];
        }

        cout << "Enter finish times: ";
        for (int i = 0; i < n; i++) {
            cin >> f[i];
        }

        sortft();
    }

    void operations() {
        selectedjobs[sc++] = 1; // First job (1-based index)
        recursiveActivitySelection(0, n);
        display();
    }

    void display() {
        cout << "Selected Activities: ";
        for (int i = 0; i < sc; i++) {
            cout << selectedjobs[i] << " ";
        }
        cout << endl;
    }

    ~Selection() {
        delete[] s;
        delete[] f;
        delete[] selectedjobs;
        delete[] counter;
    }
};

int main() {
    Selection a;
    a.operations();
    return 0;
}
