from collections import deque
import sys

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append((nx, ny))
    return cnt-1

if __name__ == "__main__":
    M, N = map(int, input().split())

    graph = []
    for i in range(N):
        graph.append(list(map(int, sys.stdin.readline().split())))

    q = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                q.append((i,j))

    result = bfs()
    flag = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                flag = 1

    if flag == 0:
        print(result)
    else:
        print(-1)
