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