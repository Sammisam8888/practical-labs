#include <iostream>
using namespace std;

class A {
public:
    void pattern() {
        char c = 'A', d = 'a', f = 'Z';
        while (c<='Z') {
            cout << c << d<<f;
            c++;
            f--;
            d++;
        }
        cout << endl;
    }

    void display() {
        pattern();
    }
};

int main() {
    A x;
    x.display();
    return 0;
}
