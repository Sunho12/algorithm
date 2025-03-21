import sys
input = sys.stdin.readline

s, e, q = input().split()
s = int(s.replace(':', ''))
e = int(e.replace(':', ''))
q = int(q.replace(':', ''))

cnt = 0
res = set()

while True:
    try:
        time, name = input().split()
        time = int(time.replace(':',''))

        if time <= s:
            res.add(name)
        elif name in res and e <= time <= q:
            res.remove(name)
            cnt+=1
    except:
        break

print(cnt)