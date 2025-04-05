import sys
import heapq
input = sys.stdin.readline

n = int(input())
pq = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(pq, (abs(x), x))
    else:
        if not pq:
            print(0)
        else:
            abs_y, y = heapq.heappop(pq)
            print(y)