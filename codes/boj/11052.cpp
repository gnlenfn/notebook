#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int price[n+1];
    int dp[1001] = {0};

    for(int i = 1; i < n+1; i++)
        cin >> price[i];

    dp[0] = 0;
    dp[1] = price[1];
    for(int i = 2; i < n+1; i++)
    {
        for(int j = 1; j <= i; j++)
        {
            dp[i] = max(dp[i-j] + price[j], dp[i]);
        }
    }         
    cout << dp[n] << endl;                                                                                                                                                                                       
}