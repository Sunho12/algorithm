import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]  # 3차원 배열

q = deque()
has_ripe = False

for z in range(h):
    for y in range(n):
        for x in range(m):
            if matrix[z][y][x] == 1:
                q.append((z, y, x))
                has_ripe = True

if not has_ripe:
    print(-1)
    sys.exit()

# 6방향 이동
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

days = -1
while q:
    for _ in range(len(q)):  # 하루 단위로 확산
        z, y, x = q.popleft()
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and matrix[nz][ny][nx] == 0:
                matrix[nz][ny][nx] = 1
                q.append((nz, ny, nx))
    days += 1

for z in range(h):
    for y in range(n):
        for x in range(m):
            if matrix[z][y][x] == 0:
                print(-1)
                sys.exit()

print(max(0, days))
