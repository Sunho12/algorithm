ir = input()
stack = []
cnt = 0
for i in range(len(ir)):
    if ir[i] == "(":  #스택에 push
        stack.append("(")
    else:
        if ir[i-1] == "(":  #레이저인 경우
            stack.pop()
            cnt += len(stack) 

        else:  #레이저가 아닌 닫는 괄호
            stack.pop()
            cnt += 1

print(cnt)