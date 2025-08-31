import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
vips = {int(input()) for _ in range(m)}

dp = [0]*(n+1)
dp[0] = 1
if n == 1:
    print(1)
    sys.exit()

dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

start = 0
end = 0
answer = 1
for i in range(1, n+1):
    if i in vips:
        end = i-1
        length = end-start
        answer *= dp[length]
        
        start = i

# 마지막 블럭
flength = n - start
answer *= dp[flength]

print(answer)