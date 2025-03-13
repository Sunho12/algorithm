import sys
from collections import deque

input = sys.stdin.readline

def play_game(n, board, cmd):
    dr = [0, -1,0,1]
    dc = [1,0,-1,0]

    snake = deque([0,0])
    board[0][0] = 1

    t=0
    head=0
    while True:
        t+=1
        nr = snake[0][0] + dr[head]
        nc = snake[0][0] + dc[head]

        if nr<0 or nr>=n or nc<0 or nc>=n or board[nr][nc] == 1:
            break
        if board[nr][nc] != 2:
            r,c = snake.pop()
            board[r][c] = 0

def solution(n,k,l,apples, rotation_t, rotation_d):
    board = [[0]* n for _ in range(n)]
    for x,y in apples:
        board[x-1][y-1] = 2
    cmd = dict(zip(rotation_t, rotation_d))

    answer = play_game(n, board, cmd)
    return answer


if __name__ == "__main__":
    # 입력
    n = int(input())
    k = int(input())
    apples = [list(map(int, input().split())) for _ in range(k)]  # 사과 위치
    l = int(input())
    rotation_t = []  # 시간
    rotation_d = []  # 방향
    for _ in range(l):  # 회전 정보
        t, d = input().split()
        rotation_t.append(int(t))
        rotation_d.append(d)

    # 연산
    answer = solution(n, k, l, apples, rotation_t, rotation_d)

    # 출력
    print(answer)