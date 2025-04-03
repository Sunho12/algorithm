#구현, 문자열
import sys
input = sys.stdin.readline

n = int(input())
exist = set()

for _ in range(n):
    words = list(input().split())
    flag = False

    for i in range(len(words)):
        if words[i][0].lower() not in exist:
            exist.add(words[i][0].lower())
            flag = True
            words[i] = '[' + words[i][0] + ']' + words[i][1:]
            print(' '.join(words))
            break

    if not flag:
        for i in range(len(words)):
            check = False
            for j in range(len(words[i])):
                if words[i][j].lower() not in exist:
                    exist.add(words[i][j].lower())
                    flag = True
                    check = True
                    words[i] = words[i][:j] + '[' + words[i][j] + ']' + words[i][j+1:]
                    print(' '.join(words))
                    break
            if check: break
    
    if not flag:
        print(' '.join(words))
