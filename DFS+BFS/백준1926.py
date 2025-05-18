import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # 세로, 가로
picture = [list(map(int, input().split())) for _ in range(n)]

def bfs(a, b):
    q = deque()
    q.append((a, b)) # 가로, 세로
    picture[b][a] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 1
    while q:
        nx, ny = q.popleft()
        for i in range(4):
            x = nx + dx[i]
            y = ny + dy[i]
            if 0 <= x < m and 0 <= y < n and picture[y][x]:
                q.append((x, y))
                picture[y][x] = 0
                cnt += 1
    return cnt

answer_cnt = 0
answer = 0
for i in range(n):
    for j in range(m):
        if picture[i][j]:
            cnt = bfs(j, i)
            answer_cnt += 1
            answer = max(answer, cnt)

print(answer_cnt)
print(answer)