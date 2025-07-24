import sys
input = sys.stdin.readline

n, game = input().strip().split()
name = set()
for _ in range(int(n)):
    name.add(input().strip())

min_cnt = 0
if game == 'Y':
    min_cnt = 1
elif game == 'F':
    min_cnt = 2
else:
    min_cnt = 3

cnt = len(name)//min_cnt

print(cnt)
