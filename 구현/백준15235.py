import sys
from collections import deque
input = sys.stdin.readline

# 큐, 1 slice
# some people > 1 slice
# compute how long

n = int(input())
c = list(map(int, input().split()))
q = deque()
ans = []
cnt = 0

for i in range(n):
    q.append([i, c[i], 0])

while q:
    cnt += 1

    now = q.popleft()
    now[1] -= 1
    now[2] = cnt
    if now[1] == 0:
        ans.append((now[0], now[2]))
    else:
        q.append(now)

ans.sort(key = lambda x: x[0])
a = []
for i in range(n):
    a.append(ans[i][1])

print(' '.join(map(str, a)))