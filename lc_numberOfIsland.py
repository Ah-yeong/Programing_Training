class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(gird)
        n = len(grid[0])

        visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if visited[i][j] == False and graph[i][j] == 1:
                    self.dfs(grid,visited,i,j)
                    cnt += 1
        return cnt
    
    def dfs(self,graph,visitedx, y):
        visited[x][y] = True

        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx< and 0<=ny<w and graph[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)
                
# bfs
'''
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M = len(grid)
        N = len(grid[0])
        visited = [[False for _ in range(N)] for _ in range(M)]
        answer = 0

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and visited[i][j] == False:
                    temp = self.bfs(grid, visited, i, j, M, N)
                    if answer < temp:
                        answer = temp
        return answer

    def bfs(self, matrix, visited, i, j, M, N):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        queue = deque()
        visited[i][j] = True
        queue.append([i, j])
        cnt = 1

        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if  0 <= nx < M and 0 <= ny < N and visited[nx][ny] == False and matrix[nx][ny] == 1:
                        visited[nx][ny] = True
                        queue.append([nx, ny])
                        cnt += 1
        return cnt
'''
