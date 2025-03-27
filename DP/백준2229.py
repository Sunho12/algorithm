import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))
dp = [0] * (n+1) # i 번째 학생까지 고려했을 때 점수차이의 최댓값
dp[0] = 0

def team_good(start, end):
    team = score[start:end]
    return max(team) - min(team)

for i in range(1, n+1):
    for j in range(i): # 0~i-1의 인덱스부터 i까지 모두 확인
        dp[i] = max(dp[i], dp[j] + team_good(j, i))

    
print(dp[n])