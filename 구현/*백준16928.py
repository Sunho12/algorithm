import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

shortcut = [list(map(int, input().split())) for _ in range(n)]
snake = [list(map(int, input().split())) for _ in range(m)]
visited = [False] * 101
q = deque()
q.append((1, 0)) #위치, cnt
visited[1] = True

while q:
    now, cnt = q.popleft()
    if now == 100:
        print(cnt)
        sys.exit()
    
    for i in range(1, 7):
        next = now + i
        if next > 100:
            continue

        for i in range(n):
            if shortcut[i][0] == next and not visited[shortcut[i][0]]:
                next = shortcut[i][1]
                visited[next] = True
                q.append((next, cnt+1))
                continue
        
        for i in range(m):
            if snake[i][0] == next and not visited[snake[i][0]]:
                next = snake[i][1]
                visited[next] = True
                q.append((next, cnt+1))
                continue
            
        if not visited[next]:
            visited[next] = True
            q.append((next, cnt+1))
            


