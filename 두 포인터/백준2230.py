import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()

start, end = 0, 1
min_dif = float('INF')

while start < n and end < n:
    dif = a[end] - a[start]
    if dif == m:
        print(m)
        sys.exit()

    if dif < m:
        end += 1
        continue

    start += 1
    min_dif = min(min_dif, dif)

print(min_dif)

# 정렬 안 했을 때 시간초과 뜸