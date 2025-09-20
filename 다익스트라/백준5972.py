import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
# n개의 헛간, 소들의 길 m개 양방향 각 길에는 c마리 소
# 소들의 길은 a와 b를 이음

# 인접행렬 -> 시간 초과
# matrix = [[float('INF')]*(n+1) for _ in range(n+1)]
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     matrix[a][b] = c
#     matrix[b][a] = c

# cow = [float('INF')]*(n+1)
# visited = [False]*(n+1)

# def check_visited():
#     for i in range(n+1):
#         if not visited[i]:
#             return False
#     return True

# def min_not():
#     ans = 0
#     m = float('INF')
#     for i in range(n+1):
#         if cow[i] < m and not visited[i]:
#             ans = i
#             m = cow[i]
#     return ans


# cow[1] = 0
# visited[1] = True
# idx = 1

# while True:
#     if check_visited():
#         break
    
#     for i in range(n+1):
#         if matrix[idx][i] != float('INF'):
#             cow[i] = min(cow[i], cow[idx]+matrix[idx][i])
    
#     idx = min_not()
#     visited[idx] = True
    

# print(cow[n])

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [float('INF')]*(n+1)
dist[1] = 0

heap = [(0, 1)] # 거리, 시작노드

while heap:
    #heapq는 항상 가장 작은 거리를 가진 노드를 꺼내줌
    #cost는 현재까지 구한 최단 거리
    #now는 현재 처리할 노드
    cost, now = heapq.heappop(heap)

    #visited와 같은 역할
    if cost > dist[now]:
        continue

    for nxt, w in graph[now]:
        new_cost = cost + w
        if new_cost < dist[nxt]:
            dist[nxt] = new_cost
            heapq.heappush(heap, (new_cost, nxt))

print(dist[n])