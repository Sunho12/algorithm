import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

#북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

matrix = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
q = deque([(r, c, d)])

while q:
    y, x, d = q.popleft()

    if matrix[y][x] == 0:
        matrix[y][x] = 2
        cnt += 1
        
    cleaned = False
    for _ in range(4):
        d = (d-1) % 4 #반시계 방향 회전
        ny, nx = y + dy[d], x + dx[d]

        # 조건 확인
        if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == 0:
            q.append((ny, nx, d))
            cleaned = True
            break
        
    if not cleaned:
        bx, by = x - dx[d], y - dy[d]
        if 0 <= by < n and 0 <= bx < m and matrix[by][bx] != 1:
            q.append((by, bx, d))
        else:
            print(cnt)
            sys.exit()





