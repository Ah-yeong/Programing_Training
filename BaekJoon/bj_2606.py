import sys
from collections import deque

def bfs(vertex):
    cnt = 0
    visited[vertex] = True

    queue = deque()
    queue.append(vertex)

    while queue:
        vertex = queue.popleft()
        for i in range(V+1):
            if adj_mat[vertex][i] == 1 and visited[i] == False:
                visited[i] = True
                cnt += 1
                queue.append(i)
    return cnt
        
if __name__ == "__main__":
    V = int(sys.stdin.readline()) 
    E = int(sys.stdin.readline()) 
    E = [list(map(int, sys.stdin.readline().split())) for _ in range(E)] 
    
    visited = [False for _ in range(V+1)] 
    adj_mat = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for edge in E:
        adj_mat[edge[0]][edge[1]] = 1
        adj_mat[edge[1]][edge[0]] = 1

    print(bfs(1))