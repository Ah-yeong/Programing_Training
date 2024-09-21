from collections import deque

V, E = map(int, input().split())

indegree = [0 for _ in range(V + 1)]
graph = {key: list() for key in range(V+1)}

for _ in range(E):
    arr = list(map(int, input().split()))
    for i in range(1, arr[0]):
        graph[arr[i]].append(arr[i+1]) # u -> v
        indegree[arr[i+1]] += 1 

result = []

def topological_sort():
    q = deque()
    
    #indegree is 0
    for i in range(1, V+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        #vertex = q.pop(0)
        vertex = q.popleft()
        result.append(vertex) #sorted
        
        for i in graph[vertex]:
            indegree[i] -= 1
            #indegree is 0
            if indegree[i] == 0: q.append(i)
            
topological_sort()

if(len(result)!=V):
    print("0")
else:
    for i in result:
        print(i)
