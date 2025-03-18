import sys
input = sys.stdin.readline

t, w = map(int, input().split())
tree = list(int(input()) for _ in range(t))

# dp[시간][움직인 수]
dp = [[0] * (w+1) for _ in range(t+1)]

#초기 위치 1번 나무
for i in range(1, t+1):
    # 한번도 안 움직인 경우
    if tree[i-1] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]
    
    # 한번 이상 움직인 경우
    for j in range(1, w+1):
        #i초에 1번나무에서 떨어지고 현재 1번에 있다면
        if tree[i-1] == 1 and j % 2 == 0:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        
        #i초에 2번나무에서 떨어지고 현재 2번에 있다면
        elif tree[i-1] == 2 and j % 2 == 1:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        
        #i초에 떨어지는 나무와 현재 위치가 다르다면
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[t]))