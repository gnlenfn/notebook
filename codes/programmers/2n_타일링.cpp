#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int dp[n+1];
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 2;

    for(int i = 3; i < n+1; i++)
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007;
    return dp[n];

}