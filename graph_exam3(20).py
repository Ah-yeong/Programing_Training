import sys

def dfs(v, target):
    visited[v] = True
    if v == target:
        return
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i, A)

input = sys.stdin.readline
A,B=map(int,input().split())

graph=[[] for _ in range(A)]
visited=[False]*A #방문 여부

for _ in range(B):
    M, N=map(int,input().split())
    graph[M].append(N)

for i in graph: #노드번호에 따라 정렬
    i.sort()

dfs(0, A-1)
print()
print(visited)
print(graph)