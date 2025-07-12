import sys
input = sys.stdin.readline

a = int(input()) # 수열 크기
num = list(map(int, input().split()))

answer = 0
dp = [0]*a
dp[0] = num[0]

for i in range(a):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i],dp[j] + num[i])
        else:
            dp[i] = max(dp[i], num[i])

print(max(dp))
