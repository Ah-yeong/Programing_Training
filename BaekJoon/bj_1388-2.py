import sys

def dfs(x,y):
    visited[x][y] = True
    d = [1, -1]

    if floor[x][y] == '-':
        for i in range(2):
            ny = y + d[i]

            if 0<= ny < M and floor[x][ny] == '-' and visited[x][ny] == False:
                dfs(x, ny)

    if floor[x][y] == '|':
        for i in range(2):
            nx = x + d[i]

            if 0<= nx < N and floor[nx][y] == '|' and visited[nx][y] == False:
                dfs(nx, y)
            
if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    floor = []
    for _ in range(N):
        floor.append(list(sys.stdin.readline()))

    visited = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if visited[i][j] == False:
                dfs(i,j)
                cnt += 1
                
    print(cnt)

