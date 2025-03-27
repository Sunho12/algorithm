import sys
input = sys.stdin.readline

s = input().strip()
size = len(s)

list = set()

for i in range(size):
    for j in range(i+1):
        list.add(s[j:i+1])

print(len(list))