import sys

def dfs(i):
    visited[i] = True
    for j in range(1, N+1):
        if matrix[i][j] == 1 and visited[j] == False:
            dfs(j)

N, M = map(int, sys.stdin.readline().split())
E = [list(map(int, input().split())) for _ in range(M)]

visited = [False for _ in range(N+1)]

matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]

for edge in E:
    matrix[edge[0]][edge[1]] = 1
    matrix[edge[1]][edge[0]] = 1

cnt = 0

for i in range(1, N+1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)