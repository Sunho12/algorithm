import sys
input = sys.stdin.readline

n = int(input())
channel = []
for _ in range(n):
    channel.append(input().strip())

idx1, idx2 = channel.index('KBS1'), channel.index('KBS2')
if idx1 > idx2:
    idx2 += 1
    
answer = []
for _ in range(idx1):
    answer.append(1)
for _ in range(idx1):
    answer.append(4)
for _  in range(idx2):
    answer.append(1)
for _ in range(idx2-1):
    answer.append(4)

print(''.join(map(str, answer)))


