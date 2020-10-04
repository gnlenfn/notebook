#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n;
    int dp[100];
    vector<int> arr;

    cin >> n;
    for (int i = 0; i < n; i++){
        int x;
        cin >> x;
        arr.emplace_back(x);
    }

    dp[0] = arr[0];
    dp[1] = max(arr[0], arr[1]);
    for(int i = 2; i < n; i++)
        dp[i] = max(dp[i-2] + arr[i], dp[i-1]);    

    cout << dp[n-1] << endl;

}