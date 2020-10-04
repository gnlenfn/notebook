#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int dp[301]={0};
    int score[301];
    for(int i = 1; i <= n; i++)
        cin >> score[i];

    dp[0] = 0;
    dp[1] = score[1];
    dp[2] = max(score[1] + score[2], score[2]);
    for(int i = 3; i <= n; i++)
    {
        dp[i] = score[i] + max(score[i-1] + dp[i-3], dp[i-2]);
    }
    cout << dp[n] << endl;
}