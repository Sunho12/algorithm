import sys
import heapq as hq

input = sys.stdin.readline

def get_min_classroom(lectures):
    lectures.sort()
    pq = [-1]

    for start, end in lectures:
        if pq[0] <= start :
            hq.heappop(pq)
        hq.heappush(pq,end)

    return len(pq)
   


if __name__ == "__main__":
    n = int(input())
    lectures = [tuple(map(int, input().split())) for _ in range(n)]

    print(get_min_classroom(lectures))