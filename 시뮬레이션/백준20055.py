import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))  # 내구도
robots = deque([False] * (2 * n))

step = 0
while True:
    step += 1

    # 1.
    belt.rotate(1)
    robots.rotate(1)
    robots[n-1] = False

    # 2.
    for i in range(n-2, -1, -1):  # 내리는 위치 전까지 (거꾸로)
        if robots[i] and not robots[i+1] and belt[i+1] >= 1:
            robots[i+1] = True
            robots[i] = False
            belt[i+1] -= 1
    robots[n-1] = False    # 이 줄을 생략해서 틀렸음

    # 3.
    if belt[0] > 0:
        robots[0] = True
        belt[0] -= 1

    # 4.
    if belt.count(0) >= k:
        print(step)
        break
