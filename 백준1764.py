import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set()
b = set()

for _ in range(n):
    a.add(input().strip())

for _ in range(m):
    b.add(input().strip())

c = a.intersection(b)
sorted_list = sorted(c)

print(len(sorted_list))
for name in sorted_list:
    print(name)