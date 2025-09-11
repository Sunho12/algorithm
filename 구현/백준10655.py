import sys
input = sys.stdin.readline

n = int(input())
cp = []
for _ in range(n):
    x, y = map(int, input().split())
    cp.append((x, y))

def cal_man(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

dist_list = []
for i in range(0, n-1):
    dist_list.append(cal_man(cp[i][0], cp[i][1], cp[i+1][0], cp[i+1][1]))

total = sum(dist_list)

answer = float('INF')
for i in range(1, n-1):
    ans = total
    ans = ans - dist_list[i-1] - dist_list[i]

    new = cal_man(cp[i-1][0], cp[i-1][1], cp[i+1][0], cp[i+1][1])
    ans += new
    
    answer = min(answer, ans)

print(answer)