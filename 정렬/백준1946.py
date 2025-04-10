import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    list = []
    for _ in range(n):
        list.append(tuple(map(int, input().split())))

    list.sort(key= lambda x: x[0])
    
    cnt = 1
    min_sec = list[0][1]
    for i in range(1, n):
        x, y = list[i][0], list[i][1]
        if y < min_sec:
            cnt += 1
        min_sec = min(min_sec, y)
    
    print(cnt)


