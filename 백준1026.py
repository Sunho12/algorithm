n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)
B.reverse()

sum = 0

for i in range(n):
    sum+=A[i]*B[i]

print(sum)