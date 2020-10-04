#include <iostream>
#include <vector>

using namespace std;

void insertion_sort(vector<int> &arr){
    for(int i = 1; i < arr.size(); i++){
        int key = arr[i];
        int j = i - 1;
        while(j >= 0 && arr[j] > key){
            arr[j+1] = arr[j];
            j -= 1;
        }
        arr[j+1] = key;
    }
}

int main(){
    vector<int> arr = {4,1,2,3,6,5};
    insertion_sort(arr);
    for(auto &e : arr)
        cout << e << " ";
    cout << endl;

    return 0;
}