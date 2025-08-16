import sys
input = sys.stdin.readline

n = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
croom = [[0]*n for _ in range(n)]
blist = []

def func1(likelist, r, c): #인접한 칸에 좋아하는 학생 수
    answer = 0
    for i in range(4):
        x = c + dx[i]
        y = r + dy[i]
        if 0 <= x < n and 0 <= y < n:
            if croom[y][x] in likelist:
                answer += 1
    return answer

def func2(r, c): #인접한 칸에 비어있는 칸수
    answer = 0
    for i in range(4):
        x = c + dx[i]
        y = r + dy[i]
        if 0 <= x < n and 0 <= y < n:
            if not croom[y][x]:
                answer += 1
    return answer

def findseat(likelist):
    seat = []
    for i in range(n):
        for j in range(n):
            if croom[j][i] == 0:
                seat.append((j, i))  # y, x

    seat.sort(key= lambda x: (
        -func1(likelist, x[0], x[1]),
        -func2(x[0], x[1]),
        x[0],
        x[1]
    ))

    return seat[0][0], seat[0][1]

for i in range(n**2):
    inp = list(map(int, input().split()))
    blist.append(inp)
    student = inp[0]
    likelist = inp[1:]

    if i == 0:
        croom[1][1] = student
    else:
        y, x = findseat(likelist)
        croom[y][x] = student

def finds(b):
    for i in range(n):
        for j in range(n):
            if croom[i][j] == b:
                return i, j

ans = 0
for b in blist:
    y, x = finds(b[0])
    a = func1(b[1:], y, x)
    if a == 0:
        continue
    else:
        ans += 10**(a-1)
print(ans)