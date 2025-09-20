import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, k, t, m = map(int, input().split())
    # 팀 개수, 문제 개수, 내 팀 ID, 로그 엔트리 개수

    score = [[0] * (k+2) for _ in range(n+1)]
    # a 팀의 b 문제 점수 : score[a][b]
    # score[a][0] 은 제출 횟수
    # socre[a][k+1] 은 마지막 제출 idx

    for idx in range(m):
        i, j, s = map(int, input().split())
        # 각 팀 ID, 문제 번호, 점수

        score[i][j] = max(score[i][j], s)
        score[i][0] += 1
        score[i][k+1] = idx
    
    answer = []
    for i in range(1, n+1):
        answer.append([sum(score[i][1:k+1]), score[i][0], score[i][k+1], i])

    answer.sort(key= lambda x: (-x[0], x[1], x[2]))

    for i in range(n):
        if answer[i][3] == t:
            print(i+1)