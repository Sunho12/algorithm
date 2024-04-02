n = int(input())
answer = 0
length = len(str(n))

if length == 1:
    answer = int(n)
else:
    answer = 9
    for i in range(2,length):
        answer += i*(9*10**(i-1))
    answer += length*(n-10**(length-1)+1)

print(answer)

