import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, p, q = map(int, input().split())
dict = {}
dict[0] = 1

def calc(i):
    if i in dict:
        return dict[i]
    
    dict[i] = calc(i // p) + calc(i // q)
    return dict[i]

print(calc(n))
