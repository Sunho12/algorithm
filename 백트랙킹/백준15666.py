import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
num = sorted(list(set(num)))
n = len(num)
seq = []

def backtracking(start_idx):
    if len(seq) == m:
        print(' '.join(map(str, seq)))
        return
    
    for i in range(start_idx, n):
        seq.append(num[i])
        backtracking(i)
        seq.pop()

        
backtracking(0)