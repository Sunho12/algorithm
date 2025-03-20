import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for _ in range(n+1)]

for j in range(10):
    dp[1][j] = 1

for i in range(2, n+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][k] for k in range(j+1))

result = sum(dp[n][j] for j in range(10))
print(result % 10007)