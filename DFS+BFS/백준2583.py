import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split()) #m:세로, n:가로
matrix = [[False]*(n) for _ in range(m)]
q = deque()
cnt = 0
answer = []

def color_box(x1, y1, x2, y2):
    for i in range(y1, y2):
        for j in range(x1, x2):
            matrix[i][j] = True

def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    box = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < m and 0 <= nx < n and not matrix[ny][nx]:
                matrix[ny][nx] = True
                q.append((ny, nx))
                box += 1
    if box == 0: box = 1
    answer.append(box)

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    color_box(x1, y1, x2, y2)

for i in range(m):
    for j in range(n):
        if not matrix[i][j]:
            q.append((i, j))
            bfs()
            cnt += 1

print(cnt)
answer.sort()
print(*answer)