import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
matrix = list(input().strip() for _ in range(N))
god_likes = {}
ans_list = []
for _ in range(K):
    data = input().rstrip()
    god_likes[data] = 0
    ans_list.append(data)


dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def solve(x, y, cnt, string):
    if cnt > 5:
        return
    
    if string in god_likes:
        god_likes[string] += 1
    
    for i in range(8):
        nx = (x + dx[i]) % N
        ny = (y + dy[i]) % M
        solve(nx, ny, cnt+1, string + matrix[nx][ny])

for i in range(N):
    for j in range(M):
        solve(i, j, 1, matrix[i][j])

    
for word in ans_list:
    print(god_likes[word])