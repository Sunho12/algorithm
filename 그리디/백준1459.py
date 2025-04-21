import sys
input = sys.stdin.readline


x, y, w, s = map(int, input().split())

# 1. 평행으로만 이동
m1 = (x+y) * w

# 2. 대각선으로만 이동
if (x + y) % 2 == 0:
    m2 = max(x, y) * s
else:
    m2 = (max(x, y)-1) * s + w

# 3. 평행이동 + 대각선이동
m3 = min(x, y) * s + (abs(x-y) * w)


print(min(m1, m2, m3))