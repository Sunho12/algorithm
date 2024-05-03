import sys
input = sys.stdin.readline

def dfs(x, y):
    

x = int(input())
for _ in range(x):
    m, n, k = map(int, input().split())
    matrix = [[0]*(m) for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        matrix[b][a] = 1
    
    answer = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                dfs(i, j)
                count += 1