import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
q = deque()
q.append(N)

visited = [0 for _ in range(100001)]

def bfs():
    while q:
        x = q.popleft()
        print(visited[:17])
        if x == K:
            return visited[x]
        for i in [x-1, x+1, 2*x]:
            if 0 <= i <= 100000 and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)
            
print(bfs())
