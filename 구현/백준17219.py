import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
pw_dict = {}

for _ in range(n):
    site, pw = map(str, input().split())
    pw_dict[site] = pw

for _ in range(m):
    input_pw = input().strip()
    print(pw_dict[input_pw])
