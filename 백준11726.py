import sys
input = sys.stdin.readline

n = int(input())
solution = [0]*(n+1)

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    solution[1] = 1
    solution[2] = 2
    for i in range(3, n+1):
        solution[i] = (solution[i-1] + solution[i-2]) % 10007
    print(solution[n])

