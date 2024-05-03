import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    if n == 1 or n == 2 or n == 3:
        print(1)
    elif n == 4 or n == 5:
        print(2)
    elif n ==6 or n == 7 or n==8:
        print(n-3)
    else:
        dp = [0]*(n+1)
        dp[1], dp[2], dp[3], dp[4], dp[5]= 1, 1, 1, 2, 2
        for i in range(6, n+1):
            dp[i] = dp[i-1] + dp[i-5]
        print(dp[n])
