#include <iostream>
using namespace std;

long long dp[101] = {0};  // int 아닌 long long으로 해야 맞다
int main()
{
    int n, i;
    cin >> n;
    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 1;
    dp[4] = 2, dp[5]=2;
    for(i = 0; i < n; i++)
    {
        int answer;
        cin >> answer;
        for(int k = 6; k <= answer; k++)
            dp[k] = dp[k-5] + dp[k-1];
        cout << dp[answer] << endl;
    }
}