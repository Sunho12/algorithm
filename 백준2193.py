import sys
input = sys.stdin.readline

n = int(input())

if n == 1 or n == 2:
    print(1)
else:
    answer = [0]*(n+1)
    answer[1] = 1
    answer[2] = 1

    for i in range(3, n+1):
        answer[i] = answer[i-1] + answer[i-2]
    print(answer[n])