import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

q = deque()
graph = [[]for i in range(N+1)]
visited = [0 for i in range(N+1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

q.append(X)

while q:
    temp = q.popleft()
    for i in graph[temp]:
        if visited[i] == 0 and i != X:
            visited[i] = visited[temp] + 1
            q.append(i)

flag = 0
for i in range(N+1):
    if visited[i] == K:
        print(i)
        flag = 1

if flag == 0:
    print("-1")