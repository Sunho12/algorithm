from collections import deque
import sys

# 빠른 입력 받기
input = sys.stdin.readline

n, q = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b, usado = map(int, input().split())
    graph[a].append((b, usado))
    graph[b].append((a, usado))


def bfs(graph, n, k, start):
    queue = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    result = 0

    while queue:
        node = queue.popleft()
        for neighbor, usado in graph[node]:
            if not visited[neighbor] and usado >= k:
                visited[neighbor] = True
                queue.append(neighbor)
                result += 1
    
    return result

output = []
for _ in range(q):
    k, v = map(int, input().split())
    output.append(str(bfs(graph, n, k, v)))

sys.stdout.write("\n".join(output) + "\n")