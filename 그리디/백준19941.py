import sys
input = sys.stdin.readline

n, k = map(int, input().split())
string = input().strip()
cnt = 0
visited = [False]*n

for i in range(n):
    if string[i] == 'P':
        start = max(0, i-k)
        end = min(i+k, n-1)
        for i in range(start, end+1):
            if string[i] == 'H' and not visited[i]:
                visited[i] = True
                cnt += 1
                break

print(cnt)
