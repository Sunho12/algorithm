import sys
from itertools import permutations
input = sys.stdin.readline

def cal(a, b, opp):
    answer = 0
    if opp == "+":
        answer = a + b
    elif opp == "-":
        answer = a - b
    elif opp == "*":
        answer = a * b
    else:
        if a < 0:  # 음수처리 해줘야함.
            return -(-a // b)
        return a // b 
    return answer

def func(a_c, opp_list):
    for i in range(1, len(a)):
        an = cal(a_c[i-1], a_c[i], opp_list[i-1])
        a_c[i] = an
    return a_c[-1]

n = int(input())
a = list(map(int, input().split()))  # 리스트
opp_i = list(map(int, input().split()))  # 연산자: +, -, x, %
opp = []
for i in range(4):
    o = ""
    if i == 0:
        o = "+"
    elif i == 1:
        o = "-"
    elif i == 2:
        o = "*"
    else:
        o = "%"
    for j in range(opp_i[i]):
        opp.append(o)

opp = list(permutations(opp, n-1))
mx = -float('INF')
mn = float('INF')
for o in opp:
    a_c = a[:]
    c = func(a_c, o)
    mx = max(mx, c)
    mn = min(mn, c)

print(mx)
print(mn)

