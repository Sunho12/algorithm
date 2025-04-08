import sys
input = sys.stdin.readline

def func(n, a_list):
    avg = sum(a_list)/len(a_list)
    cnt = 0
    money = 0
    for i in range(n):
        if a_list[i] < avg:
            cnt += 1
            money -= a_list[i]
        else:
            money += a_list[i] * cnt
            cnt = 0
    if money < 0:
        money = 0
    print(money)


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    func(n, a)