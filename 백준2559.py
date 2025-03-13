"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))
sum = []

for i in range(N-K):
    x = 0
    for j in range(K):
        x += temp[i+j]
    sum.append(x)
    
print(max(sum))
"""

import sys
input = sys.stdin.readline

N, K= map(int, input().split())
temp = list(map(int, input().split()))

result = []
result.append(sum(temp[:K]))

for i in range(N-K):
    result.append(result[i]-temp[i]+temp[i+K])

print(max(result))