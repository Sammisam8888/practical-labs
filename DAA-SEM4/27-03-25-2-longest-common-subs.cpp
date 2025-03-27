#include <iostream>
using namespace std;

class LCS{
    int m,n,**c;
    string **b;
    char *x,*y;

    void lcslength(){
        for (int i=0;i<=m;i++){
            c[i][0]=0;
            b[i][0]=" ";
        }
        for (int j=0;j<=n;j++){
            c[0][j]=0;
            b[0][j]=" ";
        }
        for (int i=1;i<=m;i++){
            for (int j=1;j<=n;j++){
                if (x[i-1]==y[j-1]){
                    c[i][j]=c[i-1][j-1]+1;
                    b[i][j]="↖"; 
                }
                else if(c[i-1][j]>=c[i][j-1]+1){
                    c[i][j]=c[i-1][j];
                    b[i][j]="↑";
                }
                else{
                    c[i][j]=c[i][j-1];
                    b[i][j]="←";
                }
            }
        }
    }
    void debugdisplay(){
        int i=m,j=n;
        cout<<"Longest common subsequence : ";
        while(i!=0 && j!=0){
            if (b[i][j]=="↑"){
                i--;
            }
            else if (b[i][j]=="←"){
                j--;
            }
            else if (b[i][j]=="↖"){
                cout<<x[i-1]<<" ";
                i--; j--;
            }
            else continue;
        }
    }
    void display(){
        cout<<"Longest common subsequence DP table : \n";
        for (int i=-1;i<=n;i++){
            
            for (int j=-1;j<=m;j++){
                if (i==-1 && j==-1){
                    cout<<"X| Y ";
                    continue;
                }
                else if(i==-1){
                    cout<<y[j]<<"   ";
                    continue;
                }
                else if (j==-1){
                    cout<<x[i]<<"   ";
                }
                else {
                    cout<<c[i][j]<<b[i][j]<<"  ";
                }
            }
            cout<<'\n';
        }
    }

public :
    LCS(){
        cout<<"Enter the size of the first subsequence : ";
        cin>>m;
        x=new char[m];
        cout<<"Enter the elements of the first subsequence : ";
        
        for (int i=0;i<m;i++){
            cin>>x[i];
        }
        cout<<"Enter the size of the second subsequence : ";
        cin>>n;
        y=new char[n];
        
        cout<<"Enter the elements of the second subsequence : ";
        for (int i=0;i<n;i++){
            cin>>y[i];
        }
        b=new string*[m+1];
        c=new int*[m+1];
        for (int i=0;i<=m;i++){
            c[i]=new int[n+1];
            b[i]=new string[n+1];
        }

    }
    void operations(){
        lcslength();
        // display();
        debugdisplay();
    }
    ~LCS() {
        for (int i = 0; i <= m; i++) {
            delete[] c[i];
            delete[] b[i];
        }
        delete[] c;
        delete[] b;
        delete[] x;
        delete[] y;
    }
};

int main(){
    LCS a;
    a.operations();
    return 0;
}