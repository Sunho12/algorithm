import sys
input = sys.stdin.readline

n = int(input())
t = [0]
p = [0]
for i in range(n):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)

dp = [0]*(n+2)
for i in range(1, n+1):
    time = t[i]
    pay = p[i]
    
    fin = i+time
    #print(i, fin)
    if fin <= n+1:
        dp[fin] = max(dp[fin], max(dp[:i+1]) + pay)

#print(dp)
print(max(dp))