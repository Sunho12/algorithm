import sys
input = sys.stdin.readline

n = int(input())
s = set()

def add(x):
    global s
    if x in s:
        return
    else:
        s.add(x)

def remove(x):
    global s
    if not x in s:
        return
    else:
        s.remove(x)

def check(x):
    global s
    if x in s:
        print(1)
    else:
        print(0)

def toggle(x):
    global s
    if x in s:
        s.remove(x)
    else:
        s.add(x)

for _ in range(n):
    temp = input().split()
    if len(temp) == 1:
        if temp[0] == "all":
            s = set(range(1, 21))
        else:
            s.clear()

    else:
        op, x = temp[0], temp[1]
        if op == "add":
            add(int(x))
        elif op == "remove":
            remove(int(x))
        elif op == "check":
            check(int(x))
        elif op == "toggle":
            toggle(int(x))


