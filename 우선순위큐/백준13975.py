import sys
import heapq
input = sys.stdin.readline

def min_cost(k, file_size):
    pq = []
    for file in file_size:
        heapq.heappush(pq, file)
    
    cost = 0
    while len(pq) > 1:
        x = heapq.heappop(pq)
        y = heapq.heappop(pq)
        sum = x + y
        cost += sum
        heapq.heappush(pq, sum)

    print(cost)


t = int(input())
for _ in range(t):
    k = int(input())
    file_size = list(map(int, input().split()))
    min_cost(k, file_size)