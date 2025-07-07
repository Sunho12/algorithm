import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

def cal_admin(student, b, c):
    student -= b
    if student <= 0:
        sub = 0
    else:
        sub = student // c
        sub_l = student % c
        if sub_l != 0:
            sub += 1
    return sub+1

count = 0
for i in range(n):
    count += cal_admin(a[i], b, c)
print(count)