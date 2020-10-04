#include <iostream>
using namespace std;

long long dp[1001][10];
int main()
{
    int n;
    cin >> n;

    for(int i = 0; i <= 9; i++)
        dp[1][i] = 1;
    

    for(int i = 2; i <= n; i++)
    {
        for(int j = 0; j <= 9; j++)
        {
            for(int k = 0; k <= j; k++)
            {
                dp[i][j] += dp[i-1][k]; // dp[i][j]는 dp[i] 전체의 합
                dp[i][j] %= 10007;
            }            
        }
    }
    long long ans = 0;
    for(int i = 0; i < 10; i++)
        ans += dp[n][i];

    cout << ans % 10007 << endl;
}