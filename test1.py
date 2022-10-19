# 2020-2-2 최대이득 구하기 dp
# 오른쪽, 아래로만 이동 가능
# 모을 수 있는 돈의 최대 금액 출력
'''
rows, cols =map(int,input().split())

dp = [[0]*(cols+1) for _ in range(rows+1)]
money = []

for i in range(rows):
    money.append(list(map(int, input().split())))

for i in range(1,rows+1):
    for j in range(1,cols+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + money[i-1][j-1]

print(dp[rows][cols])
'''

# 2020-2-3 그래프 탐색
# 방문 가능한 노드를 오름차순으로 출력
'''
import sys

def dfs(v):
    visited[v] = True
    print(v)
    arr.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

input = sys.stdin.readline
A,B=map(int,input().split())

graph=[[] for _ in range(A)]
visited=[False]*A #방문 여부

for _ in range(B):
    M, N=map(int,input().split())
    graph[M].append(N)

# for i in graph: #노드번호에 따라 정렬도 가능
# i.sort()

arr = []
dfs(0)
print(sorted(arr))
'''

'''
adj list 사용 bfs
def bfs(start):
    queue=deque([start])
    visited[start]=True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
'''