import sys
input = sys.stdin.readline

l, c = map(int, input().split())
charset = list(input().strip().split())
charset.sort()

vowels = {'a', 'e', 'i', 'o', 'u'}

def is_valid(pw):
    vow = sum(1 for char in pw if char in vowels)
    notvow = len(pw) - vow
    return vow >= 1 and notvow >= 2

def backtrack(start, path):
    if len(path) == l:
        if is_valid(path):
            print(''.join(path))
        return
    
    for i in range(start, c):
        backtrack(i+1, path + [charset[i]])
    
backtrack(0, [])