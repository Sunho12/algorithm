import sys
input = sys.stdin.readline

s = input().rstrip()
search = input().rstrip()
cnt = 0
length = len(search)
i = 0

while i < len(s):
    if s[i:i+length] == search:
        cnt += 1
        i += length
    else:
        i += 1

print(cnt)