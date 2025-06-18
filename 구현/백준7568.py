import sys
input = sys.stdin.readline

def cal_rank(i):
    w = list[i][0]
    h = list[i][1]
    cnt = 0

    for x in range(n):
        if i == x:
            continue
        c_w = list[x][0]
        c_h = list[x][1]
        if w < c_w and h < c_h:
            cnt += 1
    return (cnt+1)


n = int(input())
list = [[0]*2 for _ in range(n)]
answer = []

for i in range(n):
    x, y = map(int, input().split())
    list[i][0], list[i][1] = x, y

for i in range(n):
    rank = cal_rank(i)
    answer.append(rank)

print(' '.join(map(str, answer)))