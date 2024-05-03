def d(n):
    a = str(n)
    sum = 0
    for i in range(len(a)):
        sum += int(a[i])
    return sum+int(a)

result = []
for i in range(1, 10001):
    if d(i) <= 10000:
        result.append(d(i))

for i in range(1, 10001):
    if i not in result:
        print(i)

result = set()
for i in range(1, 10000):
    result.add(d[i])

for i in range(1, 10001):
    if i not in result:
        print(i)