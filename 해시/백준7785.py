import sys
input = sys.stdin.readline

n = int(input())
company = {}

for i in range(n):
    name, status = input().split()
    company[name] = status

list = []
for name, status in company.items():
    if status == "enter":
        list.append(name)

list.sort(reverse=True)
for name in list:
    print(name)