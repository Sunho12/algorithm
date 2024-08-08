import sys
input = sys.stdin.readline

t = int(input())

matrix = [[0]*(15) for _ in range(100)]
for i in range(15):
    matrix[0][i] = i

for i in range(1, 100):
    for j in range(1,15):
        if j == 1:
            matrix[i][j] = matrix[i-1][1]
        else:
            matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]


for _ in range(t):
    k = int(input())
    n = int(input())
    print(matrix[k][n])
