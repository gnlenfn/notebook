#include <iostream>
#include <algorithm>
using namespace std;


int dp[2][100001];
int solve(int n)
{
    for(int i = 2; i <= n; i++)
    {
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + dp[0][i];
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + dp[1][i];
    }
    return max(dp[0][n], dp[1][n]);
}


int main()
{
    int t, n;
    cin >> t;
    for (int test = 0; test < t; test++)
    {
        cin >> n;
        for(int i = 1; i <= n; i++)
            cin >> dp[0][i];
        for(int i = 1; i <= n; i++)
            cin >> dp[1][i];
    
        cout << solve(n) << endl;
    }

    
}