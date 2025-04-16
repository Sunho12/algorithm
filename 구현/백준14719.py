import sys
input = sys.stdin.readline

h, w = map(int, input().split())
world = list(map(int, input().split()))
answer = 0

for i in range(1, w-1):
    left = max(world[:i])
    right = max(world[i+1:])
    m = min(right, left)
    if m > world[i]:
        answer += (m - world[i])

print(answer)
