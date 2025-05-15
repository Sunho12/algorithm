import sys
import copy
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def bfs_game():
    game_matrix = copy.deepcopy(matrix)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    for i in range(n):
        for j in range(m):
            if game_matrix[i][j] == 2:
                q.append((j, i))
   
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and game_matrix[ny][nx] == 0:
                game_matrix[ny][nx] = 2
                q.append((nx, ny))
    
    global maxCnt
    cnt = 0

    for i in range(n):
        cnt += game_matrix[i].count(0)
    
    maxCnt = max(maxCnt, cnt)

def make_wall(cnt):
    if cnt == 3:
        bfs_game()
        return 
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                make_wall(cnt+1)
                matrix[i][j] = 0


maxCnt = 0
make_wall(0)
print(maxCnt)