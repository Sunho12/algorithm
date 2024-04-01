import sys
input = sys.stdin.readline

n,m = map(int, input().split())

my_dict = {}

for i in range(1, n+1):
    a = input().rstrip()
    my_dict[i] = a
    my_dict[a] = i

for _ in range(m):
    x = input().rstrip()
    if x.isdigit():
        print(my_dict[int(x)])
    else:
        print(my_dict[x])
        