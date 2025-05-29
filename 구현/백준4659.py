import sys
input = sys.stdin.readline

vowl = ['a', 'e', 'i', 'o', 'u']

def check1(string):
    flag = False
    for char in string:
        if char in vowl:
            flag = True
    return flag

def check2(string):
    flag = True
    list = [0]*len(string)
    for i in range(len(string)):
        if string[i] in vowl:
            list[i] = 1
        else:
            list[i] = 0

    for i in range(0, len(string)-2):
        if sum(list[i:i+3]) == 0 or sum(list[i:i+3]) == 3:
            flag = False
    return flag
        

def check3(string):
    flag = True
    for i in range(0, len(string)-1):
        if string[i] == string[i+1] and string[i] not in ['e', 'o']:
            flag = False
    return flag


while True:
    string = input().strip()
    if string == 'end':
        sys.exit()
    else:
        flag = check1(string) and check2(string) and check3(string)
        if flag:
            print('<'+string+'>'+ ' is acceptable.')
        else:
            print('<'+string+'>'+ ' is not acceptable.')
    

