import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())

b = [list(map(int, input().split())) for _ in range(h+x)]

a = [[0]* w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if i >= x and j >= y:
            a[i][j] = b[i][j] - a[i - x][j - y]
        else:
            a[i][j] = b[i][j]


for i in range(h):
    print(' '.join(map(str, a[i])))