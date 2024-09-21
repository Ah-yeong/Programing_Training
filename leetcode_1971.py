class Solution(object):
    def dfs(self, start, graph, visited):
        visited[start] = True
        
        for node in graph[start]:
            if visited[node] == False:
                self.dfs(node, graph, visited)
                
    def validPath(self, n, edges, start, end):
        if n <= 1:
            return True
        
        graph = {}
        visited = [False for _ in range(n)]
        
        for e in edges:
            if(e[0] not in graph):
                graph[e[0]] = list()
            if(e[1] not in graph):
                graph[e[1]] = list()
                
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        self.dfs(start, graph, visited)
    
        return visited[end]