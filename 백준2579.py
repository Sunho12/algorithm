n = int(input())

dp = [0]*(n+1)
stage = [0]*(n+1)
for i in range(1, n+1):
    stage[i] = int(input())

if n == 1:
    print(stage[1])
    exit()
elif n == 2:
    print(stage[1]+stage[2])
    exit()

dp[1] = stage[1]
dp[2] = stage[1] + stage[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-2]+stage[i], dp[i-3]+stage[i-1]+stage[i])

print(dp[-1])

