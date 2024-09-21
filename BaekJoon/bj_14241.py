import sys
import heapq

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

h = []

for i in num:
    heapq.heappush(h, (-i,i))

sum = 0

while len(h) != 1:
    x = heapq.heappop(h)
    y = heapq.heappop(h)

    temp = x[1]+y[1]
    heapq.heappush(h, (-temp, temp))
    
    sum += x[1] * y[1]

print(sum)