import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mile = []

for i in range(n):
    p, l = map(int, input().split())
    people = list(map(int, input().split()))
    if p < l:
        mile.append(1)
    else:
        people.sort(reverse=True)
        mile.append(people[l-1])

cnt = 0
mile.sort()

for i in range(n):
    m -= mile[i]
    if m < 0:
        break
    else:
        cnt += 1

print(cnt)
