import sys
input = sys.stdin.readline

k = input().strip()
ans = 0

while len(k):
    ans += 1
    num = str(ans)
    while len(num) and len(k):
        if num[0] == k[0]:
            k = k[1:]
        num = num[1:]

print(ans)