from collections import deque
import sys

n, k = map(int, input().split())
max_size = 100001 # 100002 이후는 탐색할 필요 없음
q = deque()
visited = [False] * max_size

visited[n] = True
q.append((n, 0))

while q:
    now, cnt = q.popleft()

    if now == k:
        print(cnt)
        sys.exit()

    for next in [ now-1, now+1, 2*now ]:
        if 0 <= next < max_size and not visited[next]:
            visited[next] = True
            q.append((next, cnt + 1))