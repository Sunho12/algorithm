import sys
input = sys.stdin.readline

INF = 1e8

visited = []
matrix = []
ans = INF

def backtracking(n, cnt, cur_city, cost):
    global ans, visisted, matrix
    if cost >= ans:
        return
    if cnt == n : #n개 도시 순회 종료
        if matrix[cur_city][0] != 0:
            ans = min(ans, cost + matrix[cur_city][0])
        return
    
    for i in range(n): # cur_city에서 도시 i로 이동
        if matrix[cur_city][i] and not visited[i]:
            visited[i] = True
            backtracking(n, cnt+1, i, cost + matrix[cur_city][i])
            visited[i] = False

def solution(n, cost):
    global ans, visited, matrix

    visited = [False] * n
    matrix = cost

    visited[0] = True
    backtracking(n, 1, 0, 0)

    return ans


if __name__ == "__main__":
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    answer = solution(n, cost)
    print(answer)