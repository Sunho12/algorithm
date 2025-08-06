import sys
from collections import deque
input = sys.stdin.readline

def cal(x, y, op):
    if op == '*':
        return x*y
    elif op == '+':
        return x+y
    elif op == '-':
        return x-y
    else:
        return x/y

n = int(input())
l = input().strip()

num = [int(input()) for _ in range(n)]

q = deque()
for i in range(len(l)):
    if l[i] in ['*', '+', '/', '-']:
        y = q.pop()
        x = q.pop()
        a = cal(x, y, l[i])
        q.append(a)
    else:
        idx = ord(l[i]) - ord('A')
        q.append(num[idx])

answer = q.pop()
print(f"{answer:.2f}")