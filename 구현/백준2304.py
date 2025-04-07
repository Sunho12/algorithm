import sys
input = sys.stdin.readline

n = int(input())
bar = [list(map(int, input().split())) for _ in range(n)]
bar.sort()
max_h = max(bar[i][1] for i in range(n))
max_i = 0
for i in range(n):
    if bar[i][1] == max_h:
        max_i = i
        break
answer = max_h
curr_y = bar[0][1]

for i in range(max_i):
    answer += curr_y * (bar[i+1][0] - bar[i][0])
    if curr_y < bar[i+1][1]:
        curr_y = bar[i+1][1]

curr_y = bar[-1][1]
for i in range(n-1, max_i, -1):
    answer += curr_y * (bar[i][0] - bar[i-1][0])
    if curr_y < bar[i-1][1]:
        curr_y = bar[i-1][1]

print(answer)
