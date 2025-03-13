n = int(input())
v = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = 1
    for next in graph[v]:
        if visited[next] == 0:
            dfs(next)

dfs(1)
print(sum(visited)-1)