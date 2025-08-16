import sys
input = sys.stdin.readline

s = []
for i in range(5):
    a = int(input())
    if a <= 40:
         a= 40
    s.append(a)

print(sum(s)//5)