import sys
from collections import OrderedDict

input = sys.stdin.readline

k, l = map(int, input().split())
students = [input().strip() for _ in range(l)]

student_dict = OrderedDict()

for student in students:
    if student in student_dict:
        del student_dict[student]
    student_dict[student] = True

success = list(student_dict.keys())

for student in success[:min(k, len(success))]:
    print(student)