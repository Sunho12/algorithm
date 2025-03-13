#import sys
#input = sys.stdin.readline

N, score, P = map(int, input().split())

if N == 0 :
    print(1)
if N > 0:
    rank = list(map(int,input().split()))

    if N == P and rank[-1] >= score:
        print(-1)
    else:
        result = N+1 #이거 빠져서 런타임에러 뜸
        for i in range(N):
            if score >= rank[i]:
                result = i+1
                break
        print(result)
    
    