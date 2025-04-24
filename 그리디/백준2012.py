import sys
input = sys.stdin.readline

n = int(input())
expect = []
answer = 0

for _ in range(n):
    expect.append(int(input()))

expect.sort()

for i in range(n):
    expect_rank = i+1
    answer += abs(expect_rank - expect[i])

print(answer)