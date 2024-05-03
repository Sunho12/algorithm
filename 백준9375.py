import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    k = int(input())
    arr = []
    result = 1
    for _ in range(k):
        item, type = input().split()
        arr.append(type)
    cnt = Counter(arr)
    for item in cnt:
        result *= (cnt[item]+1)
    print(result-1)

