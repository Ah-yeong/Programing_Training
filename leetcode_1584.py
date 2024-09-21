class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, x, y):
            x = find(parent, x)
            y = find(parent, y)
            if x < y: parent[y] = x
            else: parent[x] = y

        graph = []
        l = len(points)
        
        for i in range(l):
            for j in range(i+1, l):
                dx = abs(points[i][0] - points[j][0])
                dy = abs(points[i][1] - points[j][1])
                graph.append((i, j, dx+dy)) 
                
        parent = []
        for i in range(l):
            parent.append(i)
            
        graph = sorted(graph, key=lambda x : x[2])
        mincost = idx = cnt = 0
            
        while cnt < l-1:
            u, v, w = graph[idx]
            idx += 1

            if(find(parent, u) != find(parent, v)):
                union(parent, u,v)
                cnt += 1
                mincost += w

        return mincost