import sys
from collections import deque

input = sys.stdin.readline

def func(n, locations):
    home = locations[0]
    festival = locations[-1]
    stores = locations[1:-1]

    q = deque([home])
    visited = set([home])

    while q:
        x, y = q.popleft()
        if (x, y) == festival:
            print("happy")
            return

        for store in stores + [festival]: #시작점 제외 모든 편의점 방문
            if store not in visited and abs(store[0] - x) + abs(store[1] - y) <= 1000:
                q.append(store)
                visited.add(store)
    
    print("sad")

t = int(input())
for _ in range(t):
    n = int(input())
    locations = [tuple(map(int, input().split())) for _ in range(n+2)]
    func(n, locations)


