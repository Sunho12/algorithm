import sys
from itertools import combinations
input = sys.stdin.readline

def cal_chicken_dis(house_x, house_y, chicken):
    distance = float('INF')
    for i in range(len(chicken)):
        x, y = chicken[i][0], chicken[i][1]
        dis = abs(x - house_x) + abs(y - house_y)
        distance = min(distance, dis)
    return distance

def func(house, chicken):
    answer = 0
    for h in house:
        answer += cal_chicken_dis(h[0], h[1], chicken)
    return answer

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((j, i)) # (x,y)
        elif city[i][j] == 2:
            chicken.append((j, i)) # (x,y)

chicken_num = len(chicken)
if chicken_num <= m:
    print(func(house, chicken))
else:
    chik = combinations(chicken, m)
    min_answer = float('INF')
    for c in chik:
        f = func(house, c)
        min_answer = min(min_answer, f)
    print(min_answer)