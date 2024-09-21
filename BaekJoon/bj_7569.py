from collections import deque
import sys

def bfs():
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            x, y, z = q.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if 0<=nx<N and 0<=ny<M and 0<=nz<h and graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = 1
                    q.append((nx, ny, nz))
    return cnt-1

if __name__ == "__main__":
    M, N, h = map(int, input().split())

    graph = [[list(map(int, input().split()))for _ in range(N)] for _ in range(h)]

    q = deque()

    for k in range(h):
        for i in range(N):
            for j in range(M):
                if graph[k][i][j] == 1:
                    q.append((i,j,k))

    result = bfs()
    flag = 0

    for k in range(h):
        for i in range(N):
            for j in range(M):
                if graph[k][i][j] == 0:
                    flag = 1

    if flag == 0:
        print(result)
    else:
        print(-1)
