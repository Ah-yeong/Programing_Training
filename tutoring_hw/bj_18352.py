import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
# N : 노드의 개수 / M : 간선의 개수
# X : 출발 노드 / K : 최단 거리
# 출발노드에서부터의 최단거리가 K와 같은 노드 모두 출력 (없으면 -1 출력)

q = deque()
graph = [[]for i in range(N+1)]
visited = [0 for i in range(N+1)]

# 그래프 연결 (단방향 그래프)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)

# 시작노드
q.append(X)

#bfs
while q:
    temp = q.popleft()
    for i in graph[temp]:
        if visited[i] == 0 and i != X:
            visited[i] = visited[temp] + 1
            q.append(i)

# 시작 노드와의 최단 거리가 K와 같은 노드 출력
flag = 0
for i in range(N+1):
    if visited[i] == K:
        print(i)
        flag = 1

if flag == 0:
    print("-1")