from collections import Counter
import sys
#input = list(sys.stdin.readline().rstrip())

word = input()
word_list = list(word)  #리스트 변환
word_list.sort()   #원본 유지는 sorted()

word_count = Counter(word_list) #딕셔너리 키로 반복 가능 객체 요수 개수

#홀수인 알파벳 개수가 한개보다 많으면 불가능
odd_alphabet_cnt = 0
odd_alphabet = ''
for alphabet in word_count:
    if word_count[alphabet] % 2 ==1:
        odd_alphabet_cnt += 1
        odd_alphabet += alphabet
    if odd_alphabet_cnt >1:
        print("I'm Sorry Hansoo")
        sys.exit()

answer = ''

for i in range(0, len(word), 2):  #인덱스를 2씩 증가하면서 반복
    if word_count[word_list[i]] % 2 ==1: #홀수번 등장한 애면 개수 -1
        word_count[word_list[i]] -=1
    else:   #짝수번 등장한 경우에는 그대로 유지 후 answer에 더함
        answer += word_list[i]


tmp = answer[::-1]
answer += odd_alphabet
answer += tmp
print(answer)