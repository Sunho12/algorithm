n,m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

max_unit = min(n,m)

answer = 0
for i in range(n):
    for j in range(m):
        for k in range(max_unit):
            if ((i + k) < n) and ((j + k) < m) and (matrix[i][j] == matrix[i][j + k] == matrix[i + k][j] == matrix[i + k][j + k]):
                answer = max(answer, (k + 1)**2)
                
print(answer)