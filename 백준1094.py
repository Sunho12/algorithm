
X = int(input())

k = 64
cnt = 0

while X > 0:
    if k <= X:
        cnt += 1
        X -= k
    else:
        k /= 2
    
print(cnt)