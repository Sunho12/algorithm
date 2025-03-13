"""
from collections import Counter

n = int(input())
num = list(int(input()) for _ in range(n))

print(round(sum(num) / n))   #평균

num.sort()
print(num[n//2])   # 중앙값

cnt = sorted(Counter(num).items(), key = lambda x: (-x[1], x[0])) #최빈값
if n == 1:
    print(num[0])
else:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])


print(max(num)-min(num))  #범위
"""

import sys
import statistics as st
from collections import Counter

input = sys.stdin.readline
n = int(input())
num = [int(input()) for _ in range(n)]

print(round(st.mean(num))) # 평균
print(st.median(num)) # 중앙값

cnt = sorted(Counter(num).most_common(), key = lambda x: (-x[1], x[0])) #최빈값
if n ==1 :
    print(num[0])
else:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])

print(max(num) - min(num)) # 범위
