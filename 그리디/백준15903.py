import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(m):
    a.sort()
    x = a[0]
    y = a[1]
    a[0] = x + y
    a[1] = x + y

print(sum(a))

