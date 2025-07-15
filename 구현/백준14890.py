import sys
input = sys.stdin.readline

def if_can_line(line):
    bri = [False for _ in range(n)]
    for i in range(1, n):
        if abs(line[i] - line[i-1]) > 1:
            return False
        else:
            if (line[i-1]-line[i])==1:  # 오른쪽으로 다리
                for j in range(l):
                    if j + i >= n:
                        return False
                    if line[i] != line[i+j]:
                        return False
                    if bri[i+j]:
                        return False
                    if not bri[i+j]:
                        bri[i+j] = True
            elif (line[i-1]-line[i])==-1:
                for j in range(l):
                    if i - j < 0:
                        return False
                    if line[i-1] != line[i-1-j]:
                        return False
                    if bri[i-1-j]:
                        return False
                    if not bri[i-1-j]:
                        bri[i-1-j] = True
    return True

n, l = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
road = [[False] * n for _ in range(n)]
cnt = 0

for i in range(n):
    if if_can_line(matrix[i]):
        cnt += 1

for i in range(n):
    blist = []
    for j in range(n):
        blist.append(matrix[j][i])
    if if_can_line(blist):
        cnt += 1

print(cnt)