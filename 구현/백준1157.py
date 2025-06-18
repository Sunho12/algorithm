import sys
input = sys.stdin.readline

string = input().strip()
string = string.upper()

dict = {}
for i in range(len(string)):
    s = string[i]
    if s in dict:
        dict[s] += 1
    else:
        dict[s] = 1

dict = sorted(dict.items(), key= lambda x: -x[1])
if len(dict) > 1 and dict[0][1] == dict[1][1]:
    print("?")
else:
    print(dict[0][0])
