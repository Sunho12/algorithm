import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0]
dy = [0, 0, 1, -1, 0]


def bomb():
    for i in range(r):
        for j in range(c):
            if matrix[i][j] =='.':
                bomb_list.append([i, j, 3])
                matrix[i][j] = 'O'


r, c, n = map(int, input().split())
matrix = [list(input().strip()) for _ in range(r)]
bomb_list = []

sec = 1

for i in range(r):  # 초기
    for j in range(c):
        if matrix[i][j] == 'O':
            bomb_list.append([i, j, 2])


while sec < n:
    sec += 1

    to_explode = set()

    for b in bomb_list:
        b[2] -= 1
        if b[2] == 0:
            for i in range(5):
                nx = b[1] + dx[i]
                ny = b[0] + dy[i]
                if 0 <= nx < c and 0 <= ny < r:
                    to_explode.add((ny, nx))
    
    for y, x in to_explode:
        matrix[y][x] = '.'
    
    bomb_list = [b for b in bomb_list if b[2] > 0 and (b[0], b[1]) not in to_explode]

    
    if sec % 2 == 0:
        bomb()
    


for row in matrix:
    print(''.join(row))