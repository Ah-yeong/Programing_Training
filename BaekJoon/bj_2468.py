from collections import deque
import sys

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    check[i][j] == True
    queue.append([i, j])

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and check[nx][ny] == False:
                check[nx][ny] = True
                queue.append([nx, ny])

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    num = []
    height = max(map(max, matrix))

    for i in range(0, height+1):
        check = [[False for _ in range(N)] for _ in range(N)]
        for j in range(N):
            for k in range(N):
                if matrix[j][k] <= i:
                    check[j][k] = True

        cnt = 0
        for j in range (N):
            for k in range (N):
                if check[j][k] == False:
                    bfs(j, k)
                    cnt += 1

        num.append(cnt)

    print(max(num))