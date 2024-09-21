import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    visited[i][j] = True
    queue = deque()
    queue.append([i,j])
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append([nx, ny])
                cnt += 1
    return cnt

if __name__ == "__main__":
    M, N, K = map(int, sys.stdin.readline().split())
    visited = [[False] * N for _ in range(M)]

    for i in range(K):
        space = list(map(int, sys.stdin.readline().split()))
        for j in range(space[0], space[2]):
            for k in range(space[1], space[3]):
                visited[k][j] = True

    result = []
    for i in range(M):
        for j in range(N):
            if visited[i][j] == False:
                result.append(bfs(i,j))
    
    print(len(result))
    result.sort()
    for i in result:
        print(i, end=" ")