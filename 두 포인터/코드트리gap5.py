N = int(input())
A = list(map(int, input().split()))

# Please write your code here.
start = 0
end = 0
max_K = 0

while start <= end and end < N:
    k = end - start + 1
    flag = True
    for a in A[start:end+1]:
        if a < k:
            flag = False
    
    if flag:
        max_K = max(max_K, k)
        end += 1
    else:
        start += 1

print(max_K)
