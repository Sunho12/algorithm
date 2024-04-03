from collections import deque

k = int(input())

for i in range(k):
    n,m = map(int, input().split())
    queue = deque(map(int, input().split()))
    cnt = 0
    while queue:
        best = max(queue)
        front = queue.popleft()
        m -= 1

        if best == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        
        else:
            queue.append(front)
            if m < 0:
                m = len(queue)-1

    
    
    
            


        


