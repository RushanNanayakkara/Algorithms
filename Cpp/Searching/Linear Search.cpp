#include <iostream>

using namespace std;

int linSearch(int*,int,int);

int main(){
    int arr[] = {1,2,3,4,5};
    int len = sizeof(arr)/sizeof(arr[0]);
    cout<<linSearch(arr,len,5)<<"\n";
    return 0;
}

int linSearch(int* arr, int len, int val){
    for(int i=0; i<len; i++){
        if(arr[i]==val){
            return i;
        }
    }
    return -1;
}
