'''
프로그래머스 1844 게임 맵 최단거리

1로 된 길만 갈 수 있음, 동서남북 방향으로 한칸씩 움직임
맨 왼쪽 위칸(1,1) -> 맨 오른쪽 아래칸(n,m) 으로 갈 수 있는 칸의 개수의 최솟값

n x m 크기의 게임 맵 상태가 들어옴 ( 1<=n,m<=100 )
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
-> return : 11
'''

from collections import deque

def bfs(graph, visited, m, n):
    queue = deque()
    visited[0][0] == True
    queue.append([0, 0])
    cnt = 1
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        y, x = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == False and graph[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append([ny, nx])
                graph[ny][nx] = graph[y][x] + 1

def solution(maps):
    answer = 0
    
    m = len(maps[0])
    n = len(maps)
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    bfs(maps, visited, m, n)
    
    answer = maps[-1][-1]
    
    if visited[-1][-1] == False:
        answer = -1
        
    return answer
