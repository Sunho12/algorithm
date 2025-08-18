import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(n):
    s = input().strip()
    if s[0:4] == "push":
        opp, x = s.split()
        x = int(x)
    else:
        opp = s

    if opp == "push":
        q.append(x)
    elif opp == "pop":
        if not q:
            print(-1)
        else: print(q.popleft())
    elif opp == "size":
        print(len(q))
    elif opp == "empty":
        if not q:
            print(1)
        else: print(0)
    elif opp == "front":
        if not q:
            print(-1)
        else: print(q[0])
    elif opp == "back":
        if not q:
            print(-1)
        else: print(q[-1])