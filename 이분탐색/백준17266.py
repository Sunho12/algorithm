import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
location = list(map(int, input().split()))

def func(h):
    prev = 0 # 현재까지 밝힌 위치
    for x in location:
        if x - h > prev:
            return False
        prev = x + h
    return prev >= n # 끝까지 밝혔는가 ?

left = 0
right = n
answer = n

while left <= right:
    mid = (left+right) // 2
    if func(mid):
        answer = mid
        right = mid - 1 # 더 줄일 경우
    else:
        left = mid + 1

print(answer)
