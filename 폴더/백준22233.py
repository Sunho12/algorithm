import sys
input = sys.stdin.readline

n, m = map(int, input().split())
keyword = set(input().strip() for _ in range(n))

for _ in range(m):
    words = set(input().strip().split(","))
    keyword -= words
    print(len(keyword))