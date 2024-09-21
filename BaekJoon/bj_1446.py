import sys
from collections import deque

N, D = map(int, sys.stdin.readline().split())

q = deque()
road = []
visited = [0 for i in range(N+1)]

for _ in range(N):
    start, end, len = map(int, sys.stdin.readline().split())
    road.append([start, end, len])

dist = 0
road.sort(key=lambda x:x[0])

for i in range(N):
    d1 = d2 = 0
    if D >= road[i][0]:
        d1 += (road[i][0] + road[i][2]) - dist
        d2 += road[i][1] - dist
        dist += min(d1,d2)
        print(d1,d2,dist)
        temp = road[i][1]

dist += D - temp
print(dist)


    
