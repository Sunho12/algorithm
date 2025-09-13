import sys
input = sys.stdin.readline

# 1~8번 이동
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

def magic(cloud_list):
    ddx = [1, -1, 1, -1]
    ddy = [-1, -1, 1, 1]

    for y, x in cloud_list:
        cnt = 0

        for i in range(4):
            nx = x + ddx[i]
            ny = y + ddy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[ny][nx]:
                    cnt += 1
        matrix[y][x] += cnt

def move(d, s):
    cp = set()

    for y, x in cloud:
        ny = (y + dy[d] * s) % n
        nx = (x + dx[d] * s) % n
        y, x = ny, nx

        matrix[ny][nx] += 1
        cp.add((ny, nx))
    
    cloud.clear()
    magic(cp)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] >= 2 and (i, j) not in cp:
                cloud.append((i, j))
                matrix[i][j] -= 2
    

# m번 이동
for _ in range(m):
    d, s  = map(int, input().split())
    move(d, s)

ans = 0
for i in range(n):
    ans += sum(matrix[i])
print(ans)