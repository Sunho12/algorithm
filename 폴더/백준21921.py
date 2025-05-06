import sys
input = sys.stdin.readline

n, x = map(int, input().split())
people = list(map(int, input().split()))

curr_sum = sum(people[:x])
max_pp = curr_sum
cnt = 1

for i in range(x, n):
    curr_sum = curr_sum - people[i-x] + people[i]
    if curr_sum == max_pp:
        cnt += 1
    elif curr_sum > max_pp:
        cnt = 1
        max_pp = curr_sum
    

if max_pp == 0:
    print("SAD")
    sys.exit()
print(max_pp)
print(cnt)