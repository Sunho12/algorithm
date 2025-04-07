import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

start, end = 0, 0
cnt = 0

while end < n:
    a_sum = sum(a[start:end+1])
    #print(start, end)
    if a_sum == m:
        cnt += 1
    
    if a_sum <= m:
        end += 1
    else:
        start += 1

print(cnt)

# while start <= end 로 하면 틀림