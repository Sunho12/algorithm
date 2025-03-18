import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]  #dp[y,x,d] d:가로=0, 세로=1, 대각선=2
dp[0][1][0] = 1 # (0, 1)에 가로 방향으로 파이프 놓기

#dp 배열 채우기
for y in range(n):
    for x in range(1, n):
        # 가로
        if matrix[y][x] == 0:  # 현재 칸이 벽이 아니라면
            dp[y][x][0] += dp[y][x-1][0]  # 가로로 왔을 때
            if y > 0 and dp[y][x-1][2] > 0:
                dp[y][x][0] += dp[y][x-1][2]
            
        # 세로
        if y > 0 and matrix[y][x] == 0:
            dp[y][x][1] += dp[y-1][x][1]
            if dp[y-1][x][2] > 0:
                dp[y][x][1] += dp[y-1][x][2]

        # 대각선
        if y > 0 and matrix[y][x] == 0 and matrix[y-1][x] == 0 and matrix[y][x-1] == 0:
            dp[y][x][2] += dp[y-1][x-1][2]
            dp[y][x][2] += dp[y-1][x-1][1]
            dp[y][x][2] += dp[y-1][x-1][0]
        

print(dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2])