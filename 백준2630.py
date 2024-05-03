import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

white, blue = 0,0

def div_conq(x, y, N):
    global white, blue
    cnt = 0
    for i in range(x, x+N):
        for j in range(y, y+N):
            if matrix[i][j]:
                cnt += 1
    if not cnt:
        white += 1
    elif cnt == N*N:
        blue += 1
    else:
        div_conq(x, y, N//2)
        div_conq(x + N//2, y, N//2)
        div_conq(x, y + N//2, N//2)
        div_conq(x + N//2, y + N//2, N//2)
    return

div_conq(0, 0, n)
print(white)
print(blue)