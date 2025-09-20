import sys
input = sys.stdin.readline

n, k = map(int, input().split())
rank = []

for i in range(n):
    m = list(map(int, input().split()))
    idx = m[0]
    medal = m[1:]
    rank.append([idx, medal])

rank.sort(key= lambda x: (-x[1][0], -x[1][1], -x[1][2]))

answer = []
r = 1
same = 0
for i in range(len(rank)):
    if i == 0:
        answer.append([rank[i][0], r])
    else:
        if rank[i][1] == rank[i-1][1]:
            same += 1
            answer.append([rank[i][0], r])
        else:
            r += 1
            r += same
            same = 0
            answer.append([rank[i][0], r])

for i in range(len(answer)):
    if answer[i][0] == k:
        print(answer[i][1])