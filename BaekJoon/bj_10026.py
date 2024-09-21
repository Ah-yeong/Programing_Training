import sys

def dfs(x, y):
    visited[x][y] = True
    color = graph[x][y]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<N:
            if graph[nx][ny] == color and visited[nx][ny] == False:
                dfs(nx, ny)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    
    graph = list(list(sys.stdin.readline().split('\n')[0]) for _ in range(N))

    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                    dfs(i,j)
                    cnt += 1
    print(cnt, end = " ")

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'G':
                graph[i][j] = 'R'

    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                    dfs(i,j)
                    cnt += 1
    print(cnt)