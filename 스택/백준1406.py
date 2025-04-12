import sys
input = sys.stdin.readline

left = list(input().strip())
m = int(input())
right = []

for _ in range(m):
    command = list(input().split())
    c = command[0]

    if c == 'L' and left: # 빈 리스트를 pop하면 오류가 남
        right.append(left.pop())
    elif c == 'D' and right:
        left.append(right.pop())
    elif c == 'B' and left:
        left.pop()
    elif c == 'P':
        a = command[1]
        left.append(a)

answer = left + right[::-1]
print(''.join(answer))

# 첫 시도 : string을 슬라이싱하여 작업 -> 시간초과
# python에서는 문자열이 불변 타입이기 때문에, 문자열을 수정할 때마다 새로운 문자열을 생성해야 함
# 두번째 시도 : 리스트로 처리하면 더 효율적으로 할 수 있음 -> 그래도 시간초과
# 세번째 시도 : 두 개의 스택으로 구현

'''
슬라이싱 : 각 슬라이싱에서 새로운 문자열을 생성하므로, O(n)의 시간 복잡도 소요
리스트 : 크기가 커질 수록 중간에서 삽입 또는 삭제가 O(n)이 될 수 있음.
두 스택 : 커서를 왼쪽 또는 오른쪽으로 이동시키는 방식은 O(1)로 매우 효율적, append()와 pop() 연산은 O(1)
'''