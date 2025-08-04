MOD = 10007
def solution(n, tops):
    a = [0] * (n+1)
    b = [0] * (n+1)
    a[1] = 1
    b[1] = 3 if tops[0] == 1 else 2
    for i in range(2, n+1):
        a[i] = a[i-1] + b[i-1]
        
        if tops[i-1] == 1:
            b[i] = 2*a[i-1] + 3*b[i-1]
        else:
            b[i] = a[i-1] + 2*b[i-1]
    	
        # 이렇게 안 해주면 시간초과
        a[i] %= MOD
        b[i] %= MOD
      
    answer = a[n] + b[n]
    return answer % MOD