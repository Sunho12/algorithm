import sys
input = sys.stdin.readline

# 반죽 1개 당 필요한 재료
dough = [0.5, 0.5, 0.25, 0.0625, 0.5625]
# 팬케이크 1개 당 각 토핑에 필요한 재료
topping = [1, 30, 25, 10]

n = int(input())

for _ in range(n):
    input()
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))

    max_dough = 1000000000
    for i in range(5):
        max_dough = min(max_dough, line1[i]//dough[i])

    cnt = 0

    for i in range(4):
        cnt += line2[i]//topping[i]
    
    answer = min(max_dough, cnt)
    print(int(answer))
    