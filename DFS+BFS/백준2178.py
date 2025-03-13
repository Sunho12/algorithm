import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
distance = [[-1] * m for _ in range(n)] #최단 거리 저장 배열, 방문하지 않으면 -1 -> visited 따로 필요없음

q = deque([(0, 0)]) # 시작점
distance[0][0] = 1

while q:
    y, x = q.popleft()

    if y == n - 1 and x == m - 1:
        print(distance[y][x])
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] == 1 and distance[ny][nx] == -1:
                q.append((ny, nx))
                distance[ny][nx] = distance[y][x] + 1  # 최단 거리 갱신
