import sys
input = sys.stdin.readline

n = int(input())
request = list(map(int, input().strip().split()))
m = int(input())

if sum(request) <= m:
    print(max(request))
    sys.exit()

low = 0
high = max(request)
answer = 0

while low <= high:
    mid = (low+high) // 2

    curr_total = 0
    for req in request:
        curr_total += min(req, mid)
    
    if curr_total <= m:
        answer = mid
        low = mid+1
    else:
        high = mid-1

print(answer)