import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    p, q = map(int, input().split())
    graph[p].append(q)
    graph[q].append(p)

q = deque([(a, 0)]) # (시작 사람, 촌수)
visited = [False] * (n+1)
visited[a] = True

while q:
    person, degree = q.popleft()

    if person == b:
        print(degree)
        sys.exit()

    for next in graph[person]:
        if not visited[next]:
            visited[next] = True
            q.append((next, degree + 1))

print(-1) # 연결되지 않은 경우






    
