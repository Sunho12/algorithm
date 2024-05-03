import sys
input = sys.stdin.readline

n, k = map(int, input().split())
value = []
for _ in range(n):
    value.append(int(input()))
value.sort(reverse=True)

cnt = 0
for i in value:
    if k == 0:
        break
    cnt += k//i
    k %= i

print(cnt)