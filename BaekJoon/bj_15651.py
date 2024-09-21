import sys

def dfs(cnt):
    if(cnt == M):
        for i in num:
            print(i, end = " ")
        print()
        return
    
    for i in range(1, N+1):
        if(check[i]):
            continue
    
        num.append(i)
        dfs(cnt + 1)
        num.pop()
        check[i] = False

        
N, M = map(int, sys.stdin.readline().split())

check = [False] * (N+1)
num = []

dfs(0)