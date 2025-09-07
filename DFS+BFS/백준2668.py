import sys
sys.setrecursionlimit(10**6)  #오히려 이게 있을 때 메모리 초과가 뜨고 없으면 안 뜸
input = sys.stdin.readline

n = int(input())
graph = [0] * (n+1)
for i in range(1, n+1):
    graph[i] = int(input())
ans = []

def dfs(s, e):
    visited[s] = True
    n = graph[s]
    if not visited[n]:
        dfs(n, e)
    elif visited[n] and n==i:
        ans.append(n)

for i in range(1, n+1):
    visited = [False]*(n+1)
    dfs(i, i)

print(len(ans))
ans.sort()
for a in ans:
    print(a)