import sys
input = sys.stdin.readline
n = int(input())
switch = [0] + list(map(int, input().split()))

def toggle(i):
    if switch[i] == 0:
        switch[i] = 1
    else:
        switch[i] = 0

t = int(input())
for _ in range(t):
    sex, num = map(int, input().split())
    
    if sex == 1:
        for i in range(1, n+1):
            if i % num == 0:
                toggle(i)
    else:
        toggle(num)
        right, left = num, num
        while True:
            left -= 1
            right += 1

            if left < 1 or right > n:
                break

            if switch[left] == switch[right]:
                toggle(left)
                toggle(right)
            else:
                break

switch = switch[1:]
for i in range(n // 20 + 1):
    print(' '.join(map(str, switch[i*20:i*20+20])))
