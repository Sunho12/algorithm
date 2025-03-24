import sys
input = sys.stdin.readline

li = list(map(int, input().strip()))  # 입력받은 숫자를 리스트로 변환
size = len(li)
dp = [0] * (size + 1)

# 첫 번째 자리가 0이면 해석 불가
if li[0] == 0:
    print(0)
    exit()
else:
    dp[0] = 1
    dp[1] = 1  # 첫 번째 자리가 0이 아니면 1로 초기화

for i in range(2, size + 1):
    # 한 자릿수 처리 (li[i-1]이 0이 아니면)
    if li[i - 1] != 0:
        dp[i] += dp[i - 1]

    # 두 자릿수 처리 (10 <= 두 자리가 26 이하일 때만)
    two_digit = li[i - 2] * 10 + li[i - 1]  # 두 자리를 묶어서 숫자로 변환
    if 10 <= two_digit <= 26:
        dp[i] += dp[i - 2]

    dp[i] %= 1000000  # 결과가 너무 커지는 것을 방지하기 위해 모듈러 연산

# 최종 결과 출력
print(dp[size] % 1000000)
