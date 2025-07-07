import sys
input = sys.stdin.readline

n = int(input())  ## 학생 수 2n
student = list(map(int, input().split()))

student.sort()
answer = student[:n]

student = student[::-1]
for i in range(n):
    answer[i] += student[i]

print(min(answer))