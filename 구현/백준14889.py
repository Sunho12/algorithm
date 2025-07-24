import sys
from itertools import combinations
input = sys.stdin.readline

def team_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            a, b = team[i], team[j]
            score += s[a][b]
            score += s[b][a]
    return score

n = int(input())  #짝수
s = [list(map(int, input().split())) for _ in range(n)]
answer = float('INF')

comb = combinations(range(n), n // 2)
for teamA in comb:
    teamB = [x for x in range(n) if x not in teamA]
    scoreA = team_score(teamA)
    scoreB = team_score(teamB)
    diff = abs(scoreA - scoreB)
    answer = min(answer, diff)

    if answer == 0:
        break

print(answer)