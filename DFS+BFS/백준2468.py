import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, visited, height):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and matrix[ny][nx] > height:
            visited[ny][nx] = True
            dfs(nx, ny, visited, height)


def safe_num(height):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > height and not visited[i][j]:
                visited[i][j] = True
                dfs(j, i, visited, height)
                cnt += 1
    return cnt

result = []
max_height = max(map(max, matrix))
for h in range(max_height + 1):
    result.append(safe_num(h))
print(max(result))