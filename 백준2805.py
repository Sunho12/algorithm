"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int, input().split()))

start, end = 1, max(height)

while start <= end:
    sum = 0
    mid = (start + end) // 2

    for l in height:
        if l > mid :
            sum += (l-mid)
        if sum > m:
            break
    
    if sum < m:
        end = mid-1
    else:
        start = mid+1

print(end)
"""

import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
height = Counter(map(int, input().split()))

start = 1
end = 1000000000

while start <= end:
    mid = (start+end) // 2

    tot = sum((h-mid)*i for h, i in height.items() if h > mid)

    if tot >= m:
        start = mid+1
    else:
        end = mid-1

print(end)