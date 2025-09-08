import sys
input = sys.stdin.readline

n, k = map(int, input().split())
exer = [0] + list(map(int, input().split()))
# [0, 3, 7, 5]

def check(w, idx):
    if w - k + exer[idx] >= 500:
        return True
    else: return False

q = []
for i in range(1, n+1):
    if exer[i] >= k:
        q.append(([i], 500-k+exer[i]))

ans = 0
while q:
    li, w = q.pop()
    if len(li) == n:
        ans += 1
    else:
        for j in range(1, n+1):
            if j not in li:
                if check(w, j):
                    q.append((li+[j], w-k+exer[j]))


print(ans)