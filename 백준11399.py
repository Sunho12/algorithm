import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
result = 0

while time:
    temp = min(time)
    result += n*temp
    time.remove(temp)
    n -= 1

print(result)

"""
a = int(input())
b = list(map(int, input().split()))
c = 0
for index, i in enumerate(sorted(b)):
    c += (a-index)*i
"""