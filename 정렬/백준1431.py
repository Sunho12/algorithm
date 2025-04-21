import sys
input = sys.stdin.readline

n = int(input())
serials = [input().strip() for _ in range(n)]

def calc_sum(s):
    sum = 0
    for ch in s:
        if ch.isdigit():
            sum += int(ch)
    return sum

def serials_sort_keys(s):
    return (len(s), calc_sum(s), s)

serials.sort(key= serials_sort_keys)

for s in serials:
    print(s)