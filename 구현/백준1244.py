import sys
input = sys.stdin.readline

def toggle(i):
    if switch[i] == 1:
        switch[i] = 0
    else:
        switch[i] = 1

def girl(num):
    start = num
    end = num
    while start >= 1 and end < n and switch[start] == switch[end]:
        start -= 1
        end += 1
    return start, end

n = int(input()) # 100 이하 양의 정수
switch = list(map(int, input().split())) # 스위치 상태
n_st = int(input()) # 학생 수
st_sex = [0]*n_st # 각 학생의 성별 1:남자, 2: 여자
st_num = [0]*n_st # 각 학생이 받은 수
for i in range(n_st):
    st_sex[i], st_num[i] = map(int, input().split())


for i in range(n_st):
    sex = st_sex[i]
    num = st_num[i]
    if sex == 1:
        for j in range(1, n+1):
            if j % num  == 0:
                toggle(j-1)
        else:
            start, end = girl(num-1)
            for j in range(start, end+1):
                toggle(j)

print_n = n // 20
for i in range(print_n+1):
    print(' '.join(map(str, switch[20*i:20*i+20])))