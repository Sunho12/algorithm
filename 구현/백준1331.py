import sys
input = sys.stdin.readline

matrix = [[0]*6 for _ in range(6)]
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
sx, sy, ex, ey = 0, 0, 0, 0
bx, by = 0, 0
flag = True

def is_knight_move(x1, y1, x2, y2):
    for i in range(8):
        if x1 + dx[i] == x2 and y1 + dy[i] == y2:
            return True
    return False

for i in range(36):
    s = input().strip()
    x= int(s[1]) - 1
    y = s[0]
    if y == 'A':
        y = 0
    elif y == 'B':
        y = 1
    elif y == 'C':
        y = 2
    elif y == 'D':
        y = 3
    elif y == 'E':
        y = 4
    else:
        y = 5
    
    if i == 0:
        sx, sy = x, y
    elif i == 35:
        ex, ey = x, y
    matrix[y][x] = 1

    if i == 0:
        bx, by = x, y
        continue
    else:
        if not is_knight_move(x, y, bx, by):
            flag = False
        bx, by = x, y

answer = sum(sum(s) for s in matrix)
if not is_knight_move(ex, ey, sx, sy):
    flag = False

if answer == 36 and flag:
    print("Valid")
else:
    print("Invalid")