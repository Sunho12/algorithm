import sys
from collections import deque
input = sys.stdin.readline

n, m  = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def bfs(ix, iy):
    q = deque()
    visited = [[False]* m for _ in range(n)]
    q.append((ix, iy, 1))
    visited[iy][ix] = True

    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    while q:
        x, y, l = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if matrix[ny][nx] == 1:
                    return l

                if not visited[ny][nx] and not matrix[ny][nx]:
                    q.append((nx, ny, l+1))
                    visited[ny][nx] = True
    return 0

for i in range(n):
    for j in range(m):
        if not matrix[i][j]:
            length = bfs(j, i)
            answer = max(answer, length)

print(answer)