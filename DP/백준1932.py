import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

if n == 1:
    print(matrix[0][0])
elif n == 2:
    print(max(matrix[0][0] + matrix[1][0], matrix[0][0] + matrix[1][1]))
else:
    dp = [[0] * i for i in range(1, n+1)]
    dp[0][0] = matrix[0][0]
    dp[1][0] = dp[0][0] + matrix[1][0]
    dp[1][1] = dp[0][0] + matrix[1][1]

    for i in range(2, n):  #3번째(i=2)줄부터
        dp[i][0] = dp[i-1][0] + matrix[i][0]
        dp[i][i] = dp[i-1][i-1] + matrix[i][i]
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j-1] + matrix[i][j], dp[i-1][j] + matrix[i][j])

    print(max(dp[n-1]))