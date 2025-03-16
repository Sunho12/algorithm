import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
year = 0

def dfs(y, x):
    stack = [(y, x)]
    visited[y][x] = True
    while stack:
        cy, cx = stack.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] > 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                stack.append((ny, nx))

def split():
    global visited
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                cnt += 1
    return cnt

while True:
    if split() >= 2:
        print(year)
        break
    if not any(matrix[i][j] > 0 for i in range(n) for j in range(m)):
        print(0)
        break

    ice_cnt = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > 0:
                cnt = 0
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0 <= nx < m and 0 <= ny < n and matrix[ny][nx] == 0:
                        cnt += 1
                ice_cnt[i][j] = cnt
    for i in range(n):
        for j in range(m):
            matrix[i][j] = max(0, matrix[i][j] - ice_cnt[i][j])
        
    year += 1
    