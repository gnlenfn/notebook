import sys

n = int(sys.stdin.readline().rstrip())
storage = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n)
dp[0] = storage[0]
dp[1] = max(storage[0], storage[1])

for i in range(2, n):
    dp[i] = max(dp[i-2] + storage[i], dp[i-1])

print(dp[n-1])
