#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    int t;
    cin >> t;
    for (int test = 0; test < t; test++)
    {
        int n;
        cin >> n;
        int sticker[2][n];
        for(int i = 0; i < n; i++)
        {
            for(int j = 0; j < n; j++)
            cin >> sticker[i][j];
        }
        
        long long dp[2][n+1];
        dp[0][1] = sticker[0][1];
        dp[1][1] = sticker[1][1];
        
        for(int k = 2; k <= n; k++)
        {
            dp[0][k] = max(dp[1][k-1], dp[1][k-2]) + dp[0][k];
            dp[1][k] = max(dp[0][k-1], dp[0][k-2]) + dp[1][k];
        }
        
        cout << max(dp[0][n], dp[1][n]) << endl;
    }   
}