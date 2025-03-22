#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

class Knapsack {
    int n, capacity;
    vector<int> weights, profits;
    vector<vector<pair<int, int>>> sets;
    vector<int> selected;
    clock_t start, end;

    void getdata() {
        cout << "Enter the number of items: ";
        cin >> n;
        cout << "Enter knapsack capacity: ";
        cin >> capacity;

        weights.resize(n);
        profits.resize(n);
        selected.resize(n, 0);
        sets.resize(n + 1);

        cout << "Enter weights of items: ";
        for (int i = 0; i < n; i++) cin >> weights[i];
        cout << "Enter profits of items: ";
        for (int i = 0; i < n; i++) cin >> profits[i];
    }

    void union_sets(int index) {
        sets[index] = sets[index - 1];

        for (auto &[w, p] : sets[index - 1]) {
            int newWeight = w + weights[index - 1];
            int newProfit = p + profits[index - 1];

            if (newWeight <= capacity)
                sets[index].push_back({newWeight, newProfit});
        }
    }

    void remove_invalid_pairs(int index) {
        vector<pair<int, int>> temp;
        for (auto &[w1, p1] : sets[index]) {
            bool keep = true;
            for (auto &[w2, p2] : sets[index]) {
                if (w1 > w2 && p1 <= p2) {
                    keep = false;
                    break;
                }
            }
            if (keep) temp.push_back({w1, p1});
        }
        sets[index] = temp;
    }

    void find_max_profit() {
        int maxProfit = 0, bestIndex = -1;
        for (int i = 0; i < sets[n].size(); i++) {
            if (sets[n][i].second > maxProfit) {
                maxProfit = sets[n][i].second;
                bestIndex = i;
            }
        }

        int remWeight = sets[n][bestIndex].first;
        for (int i = n - 1; i >= 0; i--) {
            if (remWeight >= weights[i] && maxProfit - profits[i] >= 0) {
                selected[i] = 1;
                remWeight -= weights[i];
                maxProfit -= profits[i];
            }
        }

        cout << "Maximum Profit: " << sets[n][bestIndex].second << endl;
        cout << "Selected Items: ";
        for (int x : selected) cout << x << " ";
        cout << endl;
    }

    void displaytime() {
        cout << "Execution Time: " << double(end - start) / CLOCKS_PER_SEC << " seconds" << endl;
    }

public:
    void operations() {
        getdata();
        start = clock();
        sets[0].push_back({0, 0});

        for (int i = 1; i <= n; i++) {
            union_sets(i);
            remove_invalid_pairs(i);
        }

        find_max_profit();
        end = clock();
        displaytime();
    }
};

int main() {
    Knapsack k;
    k.operations();
    return 0;
}
