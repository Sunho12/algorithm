import sys

def Josephus(queue, k ):
    result = list()
    index = k-1
    while queue:
        if(len(queue) > index):
            result.append(queue.pop(index))
            index += k-1
        elif(len(queue) < index):
            index = index%len(queue)
            result.append(queue.pop(index))
            index += k-1
    return result


if __name__ == "__main__":
    n , k = map(int, input().split())
    queue = list()
    for i in range(1, n+1):
        queue.append(i)
    result = Josephus(queue, k)
    print('<', end='')
    for i in range(n):
        if (i != n-1):
            print(f'{result[i]}, ', end='')
        else:
            print(f'{result[i]}', end = '')
    print('>', end='')

