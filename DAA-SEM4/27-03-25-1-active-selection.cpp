#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Selection {
    int n;
    int *s, *f;
    vector<int> selectedJobs;

    void recursiveActivitySelection(int i, int j) {
        int m = i + 1;
        while (m < j && s[m] < f[i]) {
            m++;
        }
        if (m < j) {
            selectedJobs.push_back(m + 1); // 1-based index
            recursiveActivitySelection(m, j);
        }
    }

public:
    Selection() {
        cout << "Enter the number of activities: ";
        cin >> n;
        s = new int[n];
        f = new int[n];

        cout << "Enter start times: ";
        for (int i = 0; i < n; i++) {
            cin >> s[i];
        }

        cout << "Enter finish times: ";
        for (int i = 0; i < n; i++) {
            cin >> f[i];
        }

        // Sorting activities by finish time
        vector<pair<int, int>> activities;
        for (int i = 0; i < n; i++) {
            activities.push_back({f[i], s[i]});
        }
        sort(activities.begin(), activities.end());

        for (int i = 0; i < n; i++) {
            f[i] = activities[i].first;
            s[i] = activities[i].second;
        }
    }

    void operations() {
        selectedJobs.push_back(1); // First job (1-based index)
        recursiveActivitySelection(0, n);
        display();
    }

    void display() {
        cout << "Selected Activities: ";
        for (int job : selectedJobs) {
            cout << job << " ";
        }
        cout << endl;
    }

    ~Selection() {
        delete[] s;
        delete[] f;
    }
};

int main() {
    Selection a;
    a.operations();
    return 0;
}
