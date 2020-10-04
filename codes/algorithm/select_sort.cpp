#include <iostream>
#include <vector>
using namespace std;


int select_sort(vector<int> &arr){
    for(int i = 0; i < arr.size()-1; i++){
        int min_idx = i;
        for (int j = i; j < arr.size(); j++){
            if(arr[j] < arr[min_idx]) min_idx = j;
        }
        swap(arr[i], arr[min_idx]);
    }
    // return arr;
    for(auto &e : arr)
        cout << e << " ";
    cout << endl;
    return 0;
}

int main(){
    vector<int> arr = {4,1,2,3,6,5};
    select_sort(arr);
}