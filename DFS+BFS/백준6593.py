import sys
from collections import deque
input = sys.stdin.readline

def dfs(l, r, c, building, sx, sy, sz, ex, ey, ez):
    dz = [1, -1, 0, 0, 0, 0]
    dx = [0, 0, 1, -1, 0, 0]
    dy = [0, 0, 0, 0, 1, -1]
    visited = [[[False]*c for _ in range(r)] for _ in range(l)]
    q = deque()
    q.append((sz, sy, sx, 0))
    visited[sz][sy][sx] = True
    cnt = 0

    while q:
        nz, ny, nx, cnt = q.popleft()
        if nz == ez and ny == ey and nx == ex:
            return cnt
        for i in range(6):
            x = nx + dx[i]
            y = ny + dy[i]
            z = nz + dz[i]
            if 0 <= x < c and 0 <= y < r and 0 <= z < l and not building[z][y][x] == "#" and not visited[z][y][x]:
                q.append((z, y, x, cnt+1))
                visited[z][y][x] = True
    
    return -1

def function(l, r, c):
    building = []
    for _ in range(l):
        floor = []
        for _ in range(r):
            row = list(input().strip())
            floor.append(row)
        building.append(floor)
        _ = input()
    sx, sy, sz, ex, ey, ez = 0, 0, 0, 0, 0, 0
    for z in range(l):
        for y in range(r):
            for x in range(c):
                if building[z][y][x] == "S":
                    sx, sy, sz = x, y, z
                elif building[z][y][x] == "E":
                    ex, ey, ez = x, y, z

    answer = dfs(l, r, c, building, sx, sy, sz, ex, ey, ez)
    if answer == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {answer} minute(s).")

while True:
    lrc = input().strip()
    if not lrc:
        continue

    l, r, c = map(int, lrc.split())
    if l == 0 and r == 0 and c == 0:
        break
    function(l, r, c)