n, k = map(int, input().split())
data = ['?']*n
idx=0
check = True

for i in range(k):
    num, alphabet = input().split()
    #한바퀴 넘어가는 경우에 기존 자리에서 바뀐 차이만큼을 구하기 위해 나머지 구함
    idx = (idx+int(num)) % n   
    if data[idx] != '?':
        if data[idx] == alphabet:
            continue
        check = False
    else:
        data[idx] = alphabet

for i in range(n):
    if data[i] == '?':
        continue
    for j in range(i+1, n):
        if data[i] == data[j]:
            check = False
            break

if check:
    for _ in range(n):
        print(data[idx], end='')
        idx = (idx-1)% n
else:
    print('!')
    