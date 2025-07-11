import sys
from collections import deque
import copy
input = sys.stdin.readline


def bfs(sx, sy, visited, matrix):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((sx, sy))
    visited[sy][sx] = True

    while q:
        nx, ny = q.popleft()
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            if 0 <= x < n and 0 <= y < n:
                if not visited[y][x] and matrix[ny][nx] == matrix[y][x]:
                    q.append((x, y))
                    visited[y][x] = True
    return

n = int(input())
matrix1 = []
for _ in range(n):
    matrix1.append(list(input()))

matrix2 = copy.deepcopy(matrix1)
for i in range(n):
    for j in range(n):
        if matrix2[i][j] == "R":
            matrix2[i][j] = "G"

a1 = 0 #정상
a2 = 0 #색약
visited1 = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            a1 += 1
            bfs(j, i, visited1, matrix1)

visited2 = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            a2 += 1
            bfs(j, i, visited2, matrix2)



print(a1, a2)