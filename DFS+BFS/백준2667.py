import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

num = 0
house_cnt = []

def dfs(y, x):
    graph[y][x] = 0
    cnt = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 1:
            cnt += dfs(ny, nx)  # 재귀 호출로 연결된 집 개수 추가
    
    return cnt

for y in range(n):
    for x in range(n):
        if graph[y][x] == 1:
            num += 1
            house_cnt.append(dfs(y, x))

print(num)
house_cnt.sort()
for cnt in house_cnt:
    print(cnt)


