# 투 포인터, 슬라이딩 윈도우
import sys
from collections import Counter
input = sys.stdin.readline

n, k = map(int, input().split())
list = list(map(int, input().split()))
count = [0] * 100001
start, end = 0, 0
max_cnt = 0

while end < n:
    if count[list[end]] < k:
        count[list[end]] += 1
        end += 1
    else: # 끝 원소가 k개 이상일 때
        count[list[start]] -= 1
        start += 1
    
    max_cnt = max(max_cnt, end-start)

print(max_cnt)



