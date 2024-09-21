import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

h = []

for i in num:
    heapq.heappush(h, i)
   
for _ in range(m):
    x = heapq.heappop(h)
    y = heapq.heappop(h)
    temp = x+y
    heapq.heappush(h, temp)
    heapq.heappush(h, temp)

sum = 0

for i in range(n):
    sum += h[i]

print(sum)


