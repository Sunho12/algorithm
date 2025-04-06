import sys
import heapq
input = sys.stdin.readline

n = int(input())
pq = []
cnt = 0

for _ in range(n):
    i = int(input())
    heapq.heappush(pq, i)

while len(pq) > 1:
    x = heapq.heappop(pq)
    y = heapq.heappop(pq)
    sum = x + y
    cnt += sum
    heapq.heappush(pq, sum)

print(cnt)