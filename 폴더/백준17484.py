import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 1번째: 0왼쪽대각, 1:직선, 2:오른쪽대각
dp = [[[float('INF')]*3 for _ in range(m)] for _ in range(n)]
for i in range(m):
    for j in range(3):
        dp[0][i][j] = matrix[0][i]

for i in range(1, n):
    for j in range(m):
        # 왼쪽대각
        if j < m-1:
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + matrix[i][j]

        # 직선
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + matrix[i][j]

        if j > 0:
            dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + matrix[i][j]

ans = float('INF')
for i in range(m):
    for j in range(3):
        ans = min(ans, dp[n-1][i][j])
print(ans)