import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    k = int(input())
    if k == 1:
        print(1)
    elif k == 2:
        print(2)
    elif k == 3:
        print(4)
    else:
        answer = [0]*(k+1)
        answer[1] = 1
        answer[2] = 2
        answer[3] = 4
        for i in range(4, k+1):
            answer[i] = answer[i-1] + answer[i-2] + answer[i-3]
        print(answer[k])