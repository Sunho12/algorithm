import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
def game(w, k):
    dic = defaultdict(list)
    for i in range(len(w)):
        if w.count(w[i]) >= k:
            dic[w[i]].append(i)
    
    if not dic:
        print(-1)
    else:
        min_len = float('inf')
        max_len = 1
        
        for char in dic:
            for i in range(len(dic[char])-k+1):
                length = dic[char][i+k-1] - dic[char][i] + 1
            
                min_len = min(min_len, length)
                max_len = max(max_len, length)
        print(min_len, max_len)
            

for i in range(t):
    w = input().strip()
    k = int(input())
    game(w, k)

''' 시간 초과
def sub_game(w, k):
    length = float('inf')
    maxlength = 0

    for i in range(len(w)):
        for j in range(i, len(w)):
            substr = w[i:j+1]
            leng = len(substr)

            count = Counter(substr)
            have = False
            for char, cnt in count.items():
                if cnt == k:
                    if leng < length:
                        length = leng
                    if substr[0] == char and substr[-1] == char:
                        maxlength = max(maxlength, leng)
    
    return length, maxlength

def game(w, k):
    length, maxlength = sub_game(w, k)

    if length == float('inf'):
        print(-1)
    else:
        print(length, maxlength)

for i in range(t):
    w = input().strip()
    k = int(input())
    game(w, k)
'''