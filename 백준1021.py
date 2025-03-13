import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
num = list(map(int, input().split()))
dq = deque([i for i in range(1, n+1)])
cnt = 0

for i in num:
    while True:
        if i == dq[0]:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:
                while dq[0] != i:
                    dq.rotate(-1)
                    cnt += 1
            else:
                while dq[0] != i:
                    dq.rotate(1)
                    cnt += 1
    
print(cnt)

    
