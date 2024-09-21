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
        
    




