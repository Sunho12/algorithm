# 우선순위 큐 
import heapq
import sys
input = sys.stdin.readline

def max_fullness(t, a, b):
    visited = [[False] * 2 for _ in range(t+1)] #[fullness][물 마셨는 지]
    pq = [( -0, 0, 0)] # (-fullness, fullness, drank_water)

    max_full = 0

    while pq:
        neg_f, f, water = heapq.heappop(pq)
        visited[f][water] = True
        max_full = max(max_full, f)

        # orange
        if f + a <= t and not visited[f+a][water]:
            heapq.heappush(pq, (-(f + a), f+a, water))
        # lemon
        if f + b <= t and not visited[f+b][water]:
            heapq.heappush(pq, (-(f + b), f+b, water))
        
        if water == 0:
            new_f = f // 2
            if not visited[new_f][1]:
                heapq.heappush(pq, (-new_f, new_f, 1))

    return max_full

t, a, b = map(int, input().split())
print(max_fullness(t, a, b))
