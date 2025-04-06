import sys
import heapq
input = sys.stdin.readline

'''
# 메모리 초과 발생
# 모든 값을 heapq에 넣고, 그 후 pop -> 메모리 너무 많이 소모
n = int(input())
pq = []
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        heapq.heappush(pq, -matrix[i][j])

for i in range(n-1):
    heapq.heappop(pq)

print(-(heapq.heappop(pq)))
'''

# n번째 큰값 찾기 -> 힙 크기 n개로 유지
n = int(input())
pq = []

for _ in range(n):
    row = list(map(int, input().split()))
    for num in row:
        if len(pq) < n:
            heapq.heappush(pq, num)
        else:  # 가장 작은 걸 빼고 큰 걸 넣기
            if pq[0] < num:
                heapq.heappushpop(pq, num)

print(pq[0])
