import sys
input = sys.stdin.readline

n, s, r = map(int, input().split())
boat = [1]*(n)

l = list(map(int, input().split()))
for team in l:
    boat[team-1] -= 1

ll = list(map(int, input().split()))
for team in ll:
    boat[team-1] += 1

answer = 0
for i in range(n):
    if boat[i] >= 1:
        boat[i] -= 1
    else:
        if i == 0:
            if boat[i+1] == 2:
                boat[i+1] -= 1
            else:
                answer += 1
        elif i == n-1:
            if boat[i-1] == 1:
                boat[i-1] -= 1
            else:
                answer += 1
        else:
            if boat[i-1] == 1:
                boat[i-1] -= 1
            elif boat[i+1] == 2:
                boat[i+1] -= 1
            else:
                answer += 1

print(answer)

00103
00309
03242
01582
00438
00544
00781
00907
01004
01205
01372
01484
01694
01767
01812
01921
02042
02091
02102
02120
02129
02220
02264
02275
02301
02557
02663
02730
02734
02837
02867
02890
02932
02939
02949
02992
02999
03083
03174
03190
03201
03215
00861
00645
00451
00374
00349
00340
00254
00200