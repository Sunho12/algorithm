import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
visited = [False] * (f+1)
q = deque()

visited[s] = True
q.append((s, 0))
dx = [u, -d]

while q:
    now, cnt = q.popleft()
    if now == g:
        print(cnt)
        sys.exit()
    
    for i in range(2):
        next = now + dx[i]
        if 1 <= next <= f and not visited[next]:
            visited[next] = True
            q.append((next,cnt+1))
            
    

print("use the stairs")