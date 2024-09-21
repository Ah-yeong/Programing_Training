import sys

def dfs(x, y):
    visited[x][y] = True

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1 and visited[nx][ny] == False:
            dfs(nx, ny)


if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().split())
        
        graph = [[int(0) for _ in range(M)] for _ in range(N)]
        
        for i in range(K):
            x, y = map(int, sys.stdin.readline().split())
            graph[y][x] = int(1)
        
        visited = [[False for _ in range(M)] for _ in range(N)]

        cnt = 0

        for i in range(N):
            for j in range(M):
                if visited[i][j] == False and graph[i][j] == 1:
                    dfs(i,j)
                    cnt += 1
        print(cnt)