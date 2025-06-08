import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
vocab = {}
for _ in range(n):
    v = input().strip()
    if len(v) >= m:
        if v in vocab:
            vocab[v] += 1
        else:
            vocab[v] = 1

vocab = sorted(vocab.items(), key= lambda x : (-x[1], -len(x[0]), x[0]))

for i in vocab:
    print(i[0])