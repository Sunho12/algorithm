n = int(input())


answer = 0

for i in range(1,n+1):
    digits = [int(digit) for digit in str(i)]
    if len(digits) <= 2:
        answer += 1
    else:
        if digits[2]-digits[1] == digits[1]-digits[0]:
            answer += 1

print(answer)