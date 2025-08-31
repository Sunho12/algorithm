import sys
input = sys.stdin.readline
MOD = 1000000009

dp = [0]*(1000001)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD

t = int(input())
for i in range(t):
    ans = dp[int(input())]
    print(ans)