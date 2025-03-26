#include <iostream>
using namespace std;

class Knapsack {
    int n, W;
    int *w, *p, **dp;

public:
    Knapsack() {
        cout << "Enter number of items: ";
        cin >> n;
        cout << "Enter knapsack capacity: ";
        cin >> W;

        w = new int[n];
        p = new int[n];
        dp = new int*[n + 1];
        for (int i = 0; i <= n; i++) {
            dp[i] = new int[W + 1]{0};  // Initialize with 0
        }

        cout << "Enter weights of the items: ";
        for (int i = 0; i < n; i++)
            cin >> w[i];

        cout << "Enter profits of the items: ";
        for (int i = 0; i < n; i++)
            cin >> p[i];
    }

    int fillmatrix() {
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= W; j++) {
                if (w[i - 1] <= j)
                    dp[i][j] = max(p[i - 1] + dp[i - 1][j - w[i - 1]], dp[i - 1][j]);
                else
                    dp[i][j] = dp[i - 1][j];
            }
        }
        return dp[n][W];
    }

    void display() {
        cout << "Knapsack DP Table:\n";
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= W; j++)
                cout << dp[i][j] << "\t";
            cout << endl;
        }
    }

    void findItems() {
        cout << "Selected items (1-based index): ";
        int j = W;
        for (int i = n; i > 0; i--) {
            if (dp[i][j] != dp[i - 1][j]) {
                cout << i << " ";
                j -= w[i - 1];  // Reduce the weight
            }
        }
        cout << endl;
    }

    void operations() {
        cout << "Maximum profit: " << fillmatrix() << endl;
        display();
        findItems();
    }

    ~Knapsack() {
        delete[] w;
        delete[] p;
        for (int i = 0; i <= n; i++)
            delete[] dp[i];
        delete[] dp;
    }
};

int main() {
    Knapsack k;
    k.operations();
    return 0;
}
