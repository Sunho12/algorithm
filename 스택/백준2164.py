import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
for i in range(n):
    q.append(i+1)

while len(q) > 1:
    q.popleft()
    next = q.popleft()
    q.append(next)

answer = q.pop()
print(answer)