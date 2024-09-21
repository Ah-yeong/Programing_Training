import sys
import heapq

n = int(sys.stdin.readline())
h = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(h) == 0:
            print(0)
        else:
            temp = heapq.heappop(h)
            print(temp[1])
    else:
        heapq.heappush(h, (abs(x), x))
