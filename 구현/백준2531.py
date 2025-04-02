# 슬라이딩 윈도우
import sys
from collections import deque
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = list(int(input()) for _ in range(n))

max_sushi = 0
for i in range(n):
    if i <= n-k:
        tmp = set(sushi[i:i+k])
    else:
        tmp = set(sushi[i:])
        tmp.update(sushi[:(i+k)%n])
    tmp.add(c)
    max_sushi = max(max_sushi, len(tmp))

print(max_sushi)
