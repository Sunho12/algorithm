import sys
input = sys.stdin.readline

SIZE = 9
check_row = [[False]* (SIZE+1) for _ in range(SIZE)]
check_col = [[False]* (SIZE+1) for _ in range(SIZE)]
check_3x3 = [[False]* (SIZE+1) for _ in range(SIZE)]

def calc_area(x,y):
    return (x//3)*3 + y//3

def fill_sudoku(cnt, sudoku):
    x,y = cnt//SIZE, cnt%SIZE
    if cnt == SIZE*SIZE:
        return True
    if sudoku[x][y] > 0:
        return fill_sudoku(cnt+1, sudoku)
    
    for i in range(SIZE):
        if check_row[x][i] or check_col[y][i] or check_3x3[calc_area(x,y)][i]:
            continue
        check_row[x][i] = True
        check_col[y][i] = True
        check_3x3[calc_area(x,y)][i] = True
        sudoku[x][y] = i

        if fill_sudoku(cnt+1, sudoku):
            return True

        check_row[x][i] = False
        check_col[y][i] = False
        check_3x3[calc_area(x,y)][i] = False
        sudoku[x][y] = 0
    return False

def solution(sudoku):
    answer = [[0]*(SIZE) for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            answer[i][j] = sudoku[i][j]

            if sudoku[i][j] == 0:
                continue
            check_row[i][sudoku[i][j]]=True
            check_col[j][sudoku[i][j]]= True
            check_3x3[calc_area(i,j)][sudoku[i][j]]=True

    fill_sudoku(0, sudoku)
    return answer

if __name__ == "__main__":
    sudoku = [list(map(int, input().split())) for _ in range(SIZE)]
    for linen in solution(sudoku):
        print(*line)