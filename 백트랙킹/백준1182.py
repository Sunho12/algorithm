import sys
input = sys.stdin.readline

n, s = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
total = sum(num)

def backtrack(idx, curr_sum):
    global cnt
    if idx == n:
        return

    curr_sum += num[idx]
    if curr_sum == s:
        cnt += 1
    
    # 중간에 끊어져도 됨 -> 해당 원소를 포함할 지 말지
    backtrack(idx + 1, curr_sum)
    backtrack(idx + 1, curr_sum - num[idx])
    

backtrack(0, 0)
print(cnt)