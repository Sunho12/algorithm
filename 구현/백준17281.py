import sys
from itertools import permutations
input = sys.stdin.readline


def game(inning, clist, start):
    b1, b2, b3 = 0, 0, 0
    out = 0
    score = 0
    turn = start

    while out < 3:
        pl = clist[turn]  # 특정 번호
        action = inning[pl]

        if action == 0: # 아웃
            out += 1

        elif action == 1:
            score += b3
            b3, b2, b1 = b2, b1, 1

        elif action == 2:
            score += b3 + b2
            b3, b2, b1 = b1, 1, 0

        elif action == 3:
            score += b3 + b2 + b1
            b3, b2, b1 = 1, 0, 0

        elif action == 4: # 홈런
            score += b3 + b2 + b1 + 1
            b1, b2, b3 = 0, 0, 0
       
        turn = (turn+1) % 9

    return turn, score
        

n = int(input())
answer = []
plist = [1, 2, 3, 4, 5, 6, 7, 8]
plist_perm = permutations(plist)
innings = [list(map(int, input().split())) for _ in range(n)]

for p in plist_perm:
    s = 0
    start = 0 # clist의 인덱스
    clist = list(p[:3]) + [0] + list(p[3:])

    for inn in innings:
        start, score = game(inn, clist, start)
        s += score
    answer.append(s)

print(max(answer))

