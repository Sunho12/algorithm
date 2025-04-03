import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
truck = deque(map(int, input().split()))
in_bridge = deque([0] * w)
time = 0

while truck or sum(in_bridge) > 0:
    # 다리 위 트럭들 진행 시간 증가
    in_bridge.popleft()
    in_bridge.append(0)

    if truck:
        if sum(in_bridge) + truck[0] <= l:
            truck_w = truck.popleft()
            in_bridge[-1] = truck_w
    
    time += 1


print(time)