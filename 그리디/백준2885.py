import sys
input = sys.stdin.readline

k = int(input())

i = 0
while True:
    if 2**i >= k:
        break
    i += 1

choco = 2**i
cnt = 0
choco_left = k

while choco_left != 0:
    if choco_left < choco:
        cnt += 1
        choco /= 2
    else:
        choco_left -= choco

print(2**i, cnt)
