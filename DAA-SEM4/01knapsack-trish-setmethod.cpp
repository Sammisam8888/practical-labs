#include <iostream>
#include <ctime>
using namespace std;

class Knapsack {
    int n, capacity, **sets, *weights, *profits, *selected;
    clock_t start, end;

    void getdata() {
        cout << "Enter the number of items: ";
        cin >> n;
        cout << "Enter knapsack capacity: ";
        cin >> capacity;

        weights = new int[n];
        profits = new int[n];
        selected = new int[n]();

        sets = new int*[n + 1];
        for (int i = 0; i <= n; i++) {
            sets[i] = new int[2 * (1 << n)]; // Max possible unique weight-profit pairs
            for (int j = 0; j < 2 * (1 << n); j++) {
                sets[i][j] = -1; // Mark as empty
            }
        }

        cout << "Enter weights of items: ";
        for (int i = 0; i < n; i++) cin >> weights[i];
        cout << "Enter profits of items: ";
        for (int i = 0; i < n; i++) cin >> profits[i];
    }

    void union_sets(int index) {
        int size = 0;
        for (int i = 0; sets[index - 1][i] != -1; i += 2) {
            sets[index][size] = sets[index - 1][i];      
            sets[index][size + 1] = sets[index - 1][i + 1];
            size += 2;
        }

        for (int i = 0; sets[index - 1][i] != -1; i += 2) {
            int newWeight = sets[index - 1][i] + weights[index - 1];
            int newProfit = sets[index - 1][i + 1] + profits[index - 1];

            if (newWeight <= capacity) {
                sets[index][size] = newWeight;
                sets[index][size + 1] = newProfit;
                size += 2;
            }
        }
    }

    void remove_invalid_pairs(int index) {
        int size = 0, temp[2 * (1 << n)];
        for (int i = 0; sets[index][i] != -1; i += 2) {
            bool keep = true;
            for (int j = 0; sets[index][j] != -1; j += 2) {
                if (i != j && sets[index][j] <= sets[index][i] && sets[index][j + 1] >= sets[index][i + 1]) {
                    keep = false;
                    break;
                }
            }
            if (keep) {
                temp[size] = sets[index][i];
                temp[size + 1] = sets[index][i + 1];
                size += 2;
            }
        }

        for (int i = 0; i < size; i++) {
            sets[index][i] = temp[i];
        }
        sets[index][size] = -1; 
    }

    void find_max_profit() {
        int maxProfit = 0, bestIndex = -1;
        for (int i = 0; sets[n][i] != -1; i += 2) {
            if (sets[n][i + 1] > maxProfit) {
                maxProfit = sets[n][i + 1];
                bestIndex = i;
            }
        }

        int remWeight = sets[n][bestIndex], remProfit = maxProfit;
        for (int i = n - 1; i >= 0; i--) {
            if (remWeight >= weights[i] && remProfit >= profits[i]) {
                selected[i] = 1;
                remWeight -= weights[i];
                remProfit -= profits[i];
            }
        }

        cout << "Maximum Profit: " << maxProfit << endl;
        cout << "Selected Items: ";
        for (int i = 0; i < n; i++) cout << selected[i] << " ";
        cout << endl;
    }

    void displaytime() {
        cout << "Execution Time: " << double(end - start) / CLOCKS_PER_SEC << " seconds" << endl;
    }

public:
    void operations() {
        getdata();
        start = clock();
        sets[0][0] = 0;
        sets[0][1] = 0;
        sets[0][2] = -1;

        for (int i = 1; i <= n; i++) {
            union_sets(i);
            remove_invalid_pairs(i);
        }

        find_max_profit();
        end = clock();
        displaytime();

        delete[] weights;
        delete[] profits;
        delete[] selected;
        for (int i = 0; i <= n; i++) {
            delete[] sets[i];
        }
        delete[] sets;
    }
};

int main() {
    Knapsack k;
    k.operations();
    return 0;
}
