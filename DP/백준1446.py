import sys
input = sys.stdin.readline

n, d = map(int, input().split())
dp = [i for i in range(d+1)]
sc = []

for _ in range(n):
    s, e, l = map(int, input().split())
    if l < e-s and e <= d:
        sc.append((s, e, l))

for i in range(d+1):
    if i > 0:
        dp[i] = min(dp[i], dp[i-1] + 1)
    
    for s, e, l in sc:
        if i == s:
            dp[e] = min(dp[e], dp[s] + l)
    

print(dp[d])