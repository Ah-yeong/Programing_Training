import sys

def dfs(x,y, cnt):
    visited[x][y] = True
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < len(board) and 0<= ny < len(board[0]) and visited[nx][ny] == False:
            cnt += 1
            if board[nx][ny] == word[cnt]:
                dfs(nx, ny, cnt)
            else:
                cnt -= 1

if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = sys.stdin.readline()

    visited = [[False for _ in range(4)] for _ in range(4)]

    cnt = 0

    for i in range(3):
        for j in range(4):
            if visited[i][j] == False and word[0] == board[i][j]:
                result = dfs(i,j, cnt)
                if result == len(word):
                    print("Yes")

    print("No")