import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = [[-1] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 시작점 찾기
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            start = (i, j)
            result[i][j] = 0

def bfs(sy, sx):
    q = deque()
    visited = [[False] * (m) for _ in range(n)]
    q.append((sy, sx))
    visited[sy][sx] = True

    while q:
        y, x = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and matrix[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = True
                result[ny][nx] = result[y][x] + 1
                q.append((ny, nx))

bfs(*start)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            result[i][j] = 0

for row in result:
    print(' '.join(map(str, row)))
