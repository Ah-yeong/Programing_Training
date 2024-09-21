def DFS(computers, visited, v, n):
    visited[v] = True
    for node in range(n):
        if visited[node] == False and computers[v][node] == 1 and node != v :
                DFS(computers, visited, node, n)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if visited[i] == False:
            DFS(computers, visited, i, n)
            answer += 1
            
    return answer
