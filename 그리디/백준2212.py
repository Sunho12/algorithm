import sys
input = sys.stdin.readline


n = int(input())   #센서의 개수
k = int(input())
censer = list(map(int, input().split()))
censer.sort()
x = []

for i in range(n-1):
    x.append(censer[i+1] - censer[i])

x.sort()
print(sum(x[:n-1-(k-1)]))

"""
station.sort()
print(station)
senser = []
p = n // k
answer = 0

def cal_senser(s_list):
    cnt = len(s_list)
    s = sum(s_list)
    return s // cnt

def cal_length(sta, s_list):
    ans = 0
    for s in s_list:
        ans = max(ans, abs(sta-s))
    return ans

for i in range(k):
    idx = p * i
    temp = station[idx:idx+p]
    d = cal_senser(temp)
    print(d, cal_length(d, temp))
    answer += cal_length(d, temp)

print(answer)
"""