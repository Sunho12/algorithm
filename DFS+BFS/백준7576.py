import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())

tomato = [list(map(int, input().split())) for _ in range(n)]
q = deque()
flag = False

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            flag = True

        if tomato[i][j] == 1:
            q.append((i, j, 0))

if not flag:
    print(0)
    sys.exit()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_day = 0

while q:
    y, x, day = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < n and 0 <= nx < m and tomato[ny][nx] == 0:
            tomato[ny][nx] = 1
            q.append((ny, nx, day+1))

            max_day = max(max_day, day+1)

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0:
            print(-1)
            sys.exit()

print(day)

