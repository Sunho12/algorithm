import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
target = list(input().strip())
answer = 0

for _ in range(n-1):
    compare = target[:]
    word = input().strip()
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1
    
    if cnt <= 1 and len(compare) <= 1:
        answer += 1

print(answer)