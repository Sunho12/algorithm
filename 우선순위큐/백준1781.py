import sys
import heapq
input = sys.stdin.readline

'''
n = int(input())
pq = []
cnt = 0

for i in range(n):
    x, y = (map(int, input().split()))
    heapq.heappush(pq, (x, -y))

# 데드라인이 적게 남고, 컵라면 수가 높은 애들을 pop
time = 1
while pq:
    deadline, ramen = heapq.heappop(pq)
    if deadline < time:
        continue

    cnt += -(ramen)
    time += 1

print(cnt)
'''
# 이전에는 시점마다 개수 많은 컵라면으로 고름
# 아래는 time = 3까지 가장 큰 거 3개
n = int(input())
ramen = []
for _ in range(n):
    ramen.append(tuple(map(int, input().split())))

ramen.sort() # 기한 오름차순으로 정렬

answer = []

for deadline, ram in ramen:
    heapq.heappush(answer, ram)
    if len(answer) > deadline:
        heapq.heappop(answer)

print(sum(answer))