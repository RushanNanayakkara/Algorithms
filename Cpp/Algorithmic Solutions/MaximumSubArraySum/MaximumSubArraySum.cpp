#include <bits/stdc++.h>

using namespace std;

int maxSubArraySum(int*,int);

int main(){
    // int arr[10];
    string s;
    getline(cin,s);
    
    string delimiter = " ";
    size_t i = 0;
    while((i = s.find(delimiter))!=string::npos){
        cout<<s.substr(0,i)<<endl;
        s.erase(0,i+delimiter.length());
    }
    return 0;
}

int maxSubArraySum(int* arr,int len){
    int best = 0;
    int current = 0;
    for(int i=0; i<len; i++){
        current = max(arr[i],current+arr[i]);
        best = max(current, best);
    }
    return best;
}