import sys
input = sys.stdin.readline

string = input().strip()
a_cnt = string.count('a')

string += string
cnt = float('INF')
for i in range(len(string) - a_cnt + 1):
    cnt = min(cnt, string[i:i+a_cnt].count('b'))

print(cnt)