import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}
for i in range(n):
    name = input().rstrip()
    cnt = int(input())
    dict[name] = []
    for _ in range(cnt):
        dict[name].append(input().rstrip())

for _ in range(m):
    name = input().rstrip()
    q = int(input())
    if q == 0:
        member = sorted(dict[name])
        for m in member:
            print(m)
    else:
        for team, members in dict.items():
            if name in members:
                print(team)