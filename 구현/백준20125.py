import sys
input = sys.stdin.readline

def check_heart():
    for i in range(1, n-1):
        for j in range(1, n-1):
            if matrix[i][j] == '*' and matrix[i+1][j] == '*' and matrix[i-1][j] == '*' and matrix[i][j-1] == '*' and matrix[i][j+1] == '*':
                return i, j  # y, x
            
def check_waist(x, y):
    while matrix[y][x] == '*':
        y += 1
    return y-1

def cal_length(x, y, dx, dy):
    cnt = 0
    while 0 <= x < n and 0 <= y < n and matrix[y][x] == '*':
        cnt += 1
        x += dx
        y += dy
    return cnt

n = int(input())
matrix = [list(map(str, input().strip())) for _ in range(n)]
y, x= check_heart()
waist_y = check_waist(x, y)

left_arm = cal_length(x-1, y, -1, 0)
right_arm = cal_length(x+1, y, 1, 0)
waist = cal_length(x, y+1, 0, 1)
left_leg = cal_length(x-1, waist_y+1, 0, 1)
right_leg = cal_length(x+1, waist_y+1, 0, 1)

print(y+1, x+1)
print(left_arm, right_arm, waist, left_leg, right_leg)