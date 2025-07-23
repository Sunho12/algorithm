# cal_len에서 구할 수 없는 경우 None이 return 됨
# 이럴경우 min(answer)에서 에러가 남 -> 그래서 백준에서 런타임 에러(TypeErro)가 뜸

import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def decide_island(i, j, isl_num):
    q = deque()
    q.append((i, j))
    island.append([i, j, isl_num])
    visited[j][i] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if m[ny][nx] == 1:
                    q.append((nx, ny))
                    island.append([nx, ny, isl_num])
                    visited[ny][nx] = True
                else:
                    margin.append([nx, ny, isl_num])
                    visited[ny][nx] = True

def find_islnum(i, j):
    for isl in island:
        if isl[0] == i and isl[1] == j:
            return isl[2]

def cal_len(i, j, isl_num):
    q = deque()
    visited = [[False]* n for _ in range(n)]
    q.append((i, j, 1))
    visited[j][i] = True
    while q:
        x, y, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx]:
                if m[ny][nx] == 0:
                    q.append((nx, ny, cnt+1))
                    visited[ny][nx] = True
                elif m[ny][nx] == 1 and find_islnum(nx, ny) != isl_num:
                    return cnt


n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
island = []
margin = []
visited = [[False]*n for _ in range(n)]
isl_num = 1
for i in range(n):
    for j in range(n):
        if m[j][i] == 1 and not visited[j][i]:
            decide_island(i, j, isl_num)
            isl_num += 1

answer = []
for mar in margin:
    res = cal_len(mar[0], mar[1], mar[2])
    if res is not None:
        answer.append(res)

print(min(answer))
