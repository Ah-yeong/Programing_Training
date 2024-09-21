import sys
from collections import deque
from unittest import result

N = int(sys.stdin.readline())
graph = [list(map(int, input().split())) for _ in range(N)]

result = [[0] * N for _ in range(N)]
q = deque()

for i in range(N):
    visited = [False] * N
    q.append(i)
    while q:
        x = q.popleft()
        for j in range(N):
            if graph[x][j] == 1 and visited[j] == False:
                result[i][j] = 1
                visited[j] = True
                q.append(j)

for i in range(N):
    for j in range(N):
        print(result[i][j], end=' ')
    print("")



