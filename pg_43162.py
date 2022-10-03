'''
프로그래머스 네트워크(43162)

컴퓨터의 개수 n (1<=n<=200)
연결에 대한 정보가 담긴 2차원 배열 computers
- i번 컴퓨터와 j번 컴퓨터가 연결 되어 있으면 computers[i][j] = 1
- computers[i][i]는 항상 1

-> 네트워크의 개수를 return
'''

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