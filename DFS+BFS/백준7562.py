import sys
from collections import deque
input = sys.stdin.readline

def chess(l, now_y, now_x, goal_x, goal_y):
    chess = [[0] * l for _ in range(l)]
    dx = [1, 2, 1, 2, -1, -2, -1, -2]
    dy = [-2, -1, 2, 1, -2, -1, 2, 1]
    q = deque()
    q.append((now_y, now_x, 0))
    chess[now_y][now_x] = 1
    while q:
        y, x, cnt = q.popleft()
        if y == goal_y and x == goal_x:
            return(cnt)
        else:
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < l and 0 <= ny < l and not chess[ny][nx]:
                    q.append((ny, nx, cnt+1))
                    chess[ny][nx] = 1

t = int(input())
for _ in range(t):
    l = int(input())
    now_y, now_x = map(int, input().split())
    goal_y, goal_x  = map(int, input().split())
    print(chess(l, now_y, now_x, goal_x, goal_y))
