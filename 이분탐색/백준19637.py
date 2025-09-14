import sys
input = sys.stdin.readline

n, m = map(int, input().split())
c = []
for _ in range(n):
    char, x = input().strip().split()
    x = int(x)
    c.append([char, x])


for _ in range(m):
    ans_idx = 0
    s = 0
    e = n-1
    y = int(input())
    while s <= e:
        m = (s+e) // 2

        if y <= c[m][1]:
            ans_idx = m
            e = m-1
        else:
            s = m+1

    print(c[ans_idx][0])
