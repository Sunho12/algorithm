import sys
from collections import Counter
input = sys.stdin.readline

def func_sort(lst):
    lst = [x for x in lst if x != 0]
    cnt = Counter(lst)
    cnt_sorted = sorted(cnt.items(), key= lambda x: (x[1], x[0]))
    answer = []
    for i in range(len(cnt_sorted)):
        answer.append(cnt_sorted[i][0])
        answer.append(cnt_sorted[i][1])
    
    if len(answer) > 100:
        answer = answer[-100:]
    
    return answer
        

def func(type, matrix):
    if type == 1:   ## 모든 연산
        max_len = 0
        new_matrix = []
        for row in matrix:
            sorted_row = func_sort(row)
            max_len = max(max_len, len(sorted_row))
            new_matrix.append(sorted_row)
        for row in new_matrix:
            while len(row) < max_len:
                row.append(0)
        return new_matrix

    else:
        max_len = 0
        transposed = list(zip(*matrix))  # 열 기준으로 회전
        new_transposed = []

        for col in transposed:
            sorted_col = func_sort(list(col))
            max_len = max(max_len, len(sorted_col))
            new_transposed.append(sorted_col)
        
        for col in new_transposed:
            while len(col) < max_len:
                col.append(0)
        
        return [list(row) for row in zip(*new_transposed)]
            

r, c, k = map(int, input().split())
matrix = []
for _ in range(3):
    matrix.append(list(map(int, input().split())))
time = 0

while True:
    if r-1 < len(matrix) and c-1 < len(matrix[0]) and matrix[r-1][c-1] == k:
        print(time)
        break

    if time > 100:
        print(-1)
        break

    if len(matrix) >= len(matrix[0]):
        matrix = func(1, matrix)
    else:
        matrix = func(2, matrix)
    
    time += 1