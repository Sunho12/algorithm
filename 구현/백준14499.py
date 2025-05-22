import sys
input = sys.stdin.readline

n, m, y, x, k = map(int, input().split())
'''
북
서 동
남
좌표 : (r,c) r: 위에서부터 거리, c 서로부터 거리
  2
4 1 3
  5
  6
지금 윗면이 1 3이 동쪽, (x,y)
지도 각 칸에 정수 하나씩
주사위 굴려서 이동 -> 0이면 바닥면이 칸에 복사, 0이 아니면 칸에 있는게 주사위 바닥면으로 복사, 칸수가 0됨
주사위를 놓는 곳의 좌표 + 이동 명령이 주어졌을 때 이동할 때마다 상단에 쓰여있는 값 구하는 프로그램
'''
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

'''
1,2,3,4,5,6
동쪽: 4,2,1,6,5,3
서쪽: 3,2,6,1,5,4
남쪽: 2,6,3,4,1,5
북쪽: 5,1,3,4,6,2
'''
dice = [0, 0, 0, 0, 0, 0]

def roll(num):
    if num == 1:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]
    elif num == 2:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]
    elif num == 3:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]
    else:
        dice[0],dice[1],dice[2],dice[3],dice[4],dice[5] = dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]

def move(num):
    dx = 0
    dy = 0
    if num == 1:
        dx = 1
    elif num == 2:
        dx = -1
    elif num == 3:
        dy = -1
    else:
        dy = 1
    return dx, dy

def game(dice, x, y):
    down = 5
    up = 0

    if matrix[y][x] == 0:
        matrix[y][x] = dice[down]
    else:
        dice[down] = matrix[y][x]
        matrix[y][x] = 0
    
    answer = dice[up]
    print(answer)

command = list(map(int, input().split()))
for i in range(len(command)):
    dx, dy = move(command[i])
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx >= m or ny < 0 or ny >= n:
        continue
    else:
        roll(command[i])
        game(dice, nx, ny)
        x = nx
        y = ny