import sys
input = sys.stdin.readline


# dfs가 더 유리: 백트랙킹
r, c, k = map(int, input().split())
m = [list(input().strip()) for _ in range(r)]
answer = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False]*c for _ in range(r)]

def dfs(y, x, depth):
    global answer
    if (x, y) == (c-1, 0):
        if depth == k:
            answer += 1
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < c and 0 <= ny < r:
            if not visited[ny][nx] and m[ny][nx] != 'T':
                visited[ny][nx] = True
                dfs(ny, nx, depth+1)
                visited[ny][nx] = False
    
visited[r-1][0] = True
dfs(r-1, 0, 1)
print(answer)