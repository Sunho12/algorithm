import sys
input = sys.stdin.readline

num = str(input().strip())
n = 0

for x in num:
    x = int(x)
    if x > n: # n이 x보다 작을 경우 -> 그대로 한자리수
        n = x
    elif x == 0:  # x가 0이면 그 다음 10의 배수
        n_10 = n // 10
        n = 10 * (n_10 + 1)
    elif (n % 10) < x:
        n = 10 * (n // 10) + x
    elif (n % 10) > x:
        a = x * 10
        b = 10 * (n // 10 + 1) + x
        if a > n:
            n = min(a, b)
        else: n = b
    elif (n % 10) == x:
        a = n + 1
        b = 10 * (n // 10 + 1) + x
        n = min(a, b)
    print(n)

print(n)