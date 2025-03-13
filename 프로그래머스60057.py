def get_shortened_length(target, unit_length):
    length = len(target)
    new_length = length
    prev_substr = ""  # 기존 문자열
    count = 1 # 반복 횟수

    # 부분 문자열 인덱스 [left, right]
    left = 0
    right = unit_length

    while right <= length:
        curr_substr = target[left:right]

        if prev_substr == curr_substr:
            count += 1
        else:
            if count >1:
                new_length += len(str(count))
                new_length -= (count-1)*unit_length

            prev_substr = curr_substr
            count =1
        
        left += unit_length
        right += unit_length

    if count > 1:
        new_length += len(str(count))
        new_length -= (count-1)* unit_length

    return new_length


def solution(given_str):
    answer = len(given_str)
    for k in range(1, len(given_str) // 2 + 1 ):  #k 단위길이
        answer = min(answer, get_shortened_length(given_str, k))
    return answer
