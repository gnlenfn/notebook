def solution(x):
    n = x // 10

    dp = [0] * 31
    dp[1] = 1
    dp[2] = 3

    for i in range(3, len(dp)):
        dp[i] = dp[i-1] + 2 * dp[i-2]

    return dp[n]


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    print('#%d %s'%(test_case, solution(n)))