#include <iostream>
#include <limits.h>
#include <ctime>
using namespace std;

class Matrix
{
private:
    int n;
    int **t;
    int **m;
    int **s;
    double timediff, start, end;

    void checkMultiplication()
    {
        for (int i = 1; i < n; i++)
        {
            if (t[i][1] != t[i + 1][0]) // t[n-1][1] = = t [n][0]
            {
                cout << "Error: Cannot perform chain matrix multiplication due to A" << i << " and A" << i + 1 << " having mismatched columns and rows." << endl;
                exit(0);
            }
        }
    }

    void matrixChainMultiplication()
    {
        for (int i = 1; i <= n; i++)
        {
            m[i][i] = 0;
        }

        for (int l = 2; l <= n; l++)
        {
            for (int i = 1; i <= n - l + 1; i++)
            {
                int j = i + l - 1;
                m[i][j] = INT_MAX;
                for (int k = i; k <= j - 1; k++)
                {
                    int q = m[i][k] + m[k + 1][j] + t[i - 1][0] * t[k][1] * t[j][1];
                    if (q < m[i][j])
                    {
                        m[i][j] = q;
                        s[i][j] = k;
                    }
                }
            }
        }
    }

    void printOptimalParenthesis(int i, int j)
    {
        if (i == j)
        {
            cout << "A" << i;
        }
        else
        {
            cout << "(";
            printOptimalParenthesis(i, s[i][j]);
            printOptimalParenthesis(s[i][j] + 1, j);
            cout << ")";
        }
    }
    void displaymatrix(int **arr)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                cout << arr[i][j] << " ";
            }
            cout << endl;
        }
    }
    void display()
    {
        cout << "Minimum number of scalar multiplications: " << m[1][n] << endl;
        cout << "Optimal parenthesization: ";
        printOptimalParenthesis(1, n);
        cout << endl;

        cout << "Start time : " << start << " seconds \n";
        cout << "End time : " << end << " seconds \n";
        cout << "Total time taken : " << timediff << " seconds \n\n";

        cout << "After Operations M matrix : \n";
        displaymatrix(m);

        cout << "After Operations S matrix : \n";
        displaymatrix(s);
    }

public:
    Matrix()
    {
        cout << "Enter the number of matrices: ";
        cin >> n;
        t = new int *[n + 1];
        m = new int *[n + 1];
        s = new int *[n + 1];
        for (int i = 0; i <= n; i++)
        {
            m[i] = new int[n + 1];
            s[i] = new int[n + 1];
            t[i] = new int[2];
        }
        cout << "Enter the number of Rows and Columns :\n";
        for (int i = 1; i <= n; i++)
        {
            cout << "For Matrix " << i << " :";
            cin >> t[i][0] >> t[i][1];
        }
    }
    ~Matrix()
    {
        for (int i = 0; i <= n; i++)
        {
            delete[] m[i];
            delete[] s[i];
            delete[] t[i];
        }
        delete[] m;
        delete[] s;
        delete[] t;
    }

    void operations()
    {
        checkMultiplication();
        start = (double)clock() / CLOCKS_PER_SEC;
        matrixChainMultiplication();
        end = (double)clock() / CLOCKS_PER_SEC;
        timediff = end - start;
        display();
    }
};

int main()
{
    Matrix mcm;
    mcm.operations();
    return 0;
}