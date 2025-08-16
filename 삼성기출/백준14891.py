import sys
input = sys.stdin.readline


#12시 방향부터 시계 방향
#N극 0, S극 1
c = [list(input().strip()) for _ in range(4)]

idx = [0, 0, 0, 0]

def is_different(num1, num2):
    left = c[num1][(idx[num1] + 2) % 8]
    right = c[num2][(idx[num2] - 2) % 8]
    return left != right

def rotate(num, d):
    idx[num] = (idx[num] - d) % 8

k = int(input()) # 회전 횟수
for _ in range(k):
    num, d = map(int, input().split())
    num -= 1

    rotate_dir = [0, 0, 0, 0]
    rotate_dir[num] = d

    #왼쪽 방향
    for i in range(num-1, -1, -1):
        if is_different(i, i+1):
            rotate_dir[i] = -rotate_dir[i+1]
        else:
            break
    
    #오른쪽
    for i in range(num+1, 4):
        if is_different(i-1, i):
            rotate_dir[i] = -rotate_dir[i-1]
        else:
            break

    for i in range(4):
        if rotate_dir[i] != 0:
            rotate(i, rotate_dir[i])


answer = 0
if c[0][idx[0]] == '1':
    answer += 1
if c[1][idx[1]] == '1':
    answer += 2
if c[2][idx[2]] == '1':
    answer += 4
if c[3][idx[3]] == '1':
    answer += 8

print(answer)