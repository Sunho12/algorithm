import sys
input = sys.stdin.readline

n = int(input())
chains = list(map(int, input().split()))
chains.sort()

chainCnt = n
tiedChains = 1

for chain in chains:
    if tiedChains + chain >= chainCnt:
        break
    else:
        tiedChains += chain
        chainCnt -= 1

print(chainCnt - 1)