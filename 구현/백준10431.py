import sys

input = sys.stdin.readline

def func(num):
    num = num[::-1]
    line = []
    cnt = 0
    while len(num) > 0:
        now = num.pop()
        if len(line) == 0:
            line.append(now)
        elif max(line) < now:
            line.append(now)
        else:
            for i in range(len(line)):
                if line[i] > now:
                    idx = i
                    break
            cnt += (len(line) - idx)
            line = line[:i] + [now] + line[i:]
    return cnt

p = int(input())
for _ in range(p):
    t_num = list(map(int, input().split()))
    t = t_num[0]
    num = t_num[1:]
    answer = func(num)
    print(t, answer)