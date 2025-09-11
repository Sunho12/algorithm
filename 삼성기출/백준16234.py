import sys
from collections import deque
input = sys.stdin.readline

n, l, r = map(int, input().split())
# nxn 땅, 각각의 땅에는 하나의 나라, A[r][c] 명
matrix = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(sy, sx, visited):
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = True
    union = [(sy, sx)]
    total = matrix[sy][sx]

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if l <= abs(matrix[ny][nx] - matrix[y][x]) <= r:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    union.append((ny, nx))
                    total += matrix[ny][nx]

    if len(union) > 1:
        for y, x in union:
            matrix[y][x] = int(total / len(union))
        return True
    return False


while True:
    visited = [[False]*n for _ in range(n)]
    moved = False
    
    # 인구이동
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    moved = True
    
    if not moved:
        break

    ans += 1

print(ans)