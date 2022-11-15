'''
컴퓨터를 연결하는데 필요한 비용이 주어졌을 때 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력

N : 컴퓨터의 수
M : 연결할 수 있는 선의 수

M개의 줄에 다음과 같은 정보가 입력됨
-> 컴퓨터1, 컴퓨터2, 연결 비용
'''

import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x < y: parent[y] = x
    else: parent[x] = y

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())

graph = []
cnt = idx = 0

for i in range(E):
    A, B, W = map(int, sys.stdin.readline().split())
    graph.append((A, B, W))

parent = []

for i in range(0, V+1):
    parent.append(i)

graph = sorted(graph, key=lambda x : x[2])
mincost = 0

while cnt < V-1:
    u, v, w = graph[idx]
    idx += 1

    if(find(parent, u) != find(parent, v)):
        union(parent, u,v)
        cnt += 1
        mincost += w

print(mincost)