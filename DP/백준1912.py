import sys
input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))
dp = [0] * (n)
dp[0] = list[0]

for i in range(1, n):
    dp[i] = max(list[i], list[i] + dp[i-1])

print(max(dp))
