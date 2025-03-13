import sys
input = sys.stdin.readline

n = int(input())
d = [0]*1000001

for i in range(2, n+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1]+1
    # 현재의 수가 2의 배수
    if i % 2 == 0 :
        d[i] = min(d[i], d[i//2] + 1)
    # 현재의 수가 3의 배수
    if i % 3 == 0 :
        d[i] = min(d[i], d[i//3] + 1)

print(d[n])


