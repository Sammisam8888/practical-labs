#include<bits/stdc++.h>
using namespace std;
int main(){
    string s;
    stack<char>st;
    cout<<"Enter a string :";
    cin>>s;
    int state=0;
    int i=0;
    for(i=0;i<s.length();i++){
        char c=s[i];
        switch(state){
            case 0:
                if(!(st.empty())){
                    if(st.top()=='1' && c=='0'){
                        state=1;
                        st.pop();
                    }
                    else st.push(c);
                }
                else if(c=='0')st.push(c);
                break;
            case 1:
                if(c!=st.top())st.pop();
                else state=-1;
                break;
        }
        if(state==-1)break;
    }
    if(st.empty() && i==s.length()) cout<<"The string is accepted.\n";
    else cout<<"The string is not accepted.\n";
    return 0;
}