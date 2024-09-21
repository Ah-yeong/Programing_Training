import sys

def dfs(cnt):
    if(cnt == M):
        for i in num:
            print(i, end = " ")
        print()
        return
    
    for i in range(0, N):
        temp = n[i]
        if(check[temp]):
            continue

        check[temp] = True
        num.append(temp)
        dfs(cnt + 1)
        num.pop()
        check[temp] = False

N, M = map(int, sys.stdin.readline().split())
n = (list(map(int, sys.stdin.readline().split())))
n.sort()

check = [False] * (n[-1]+1)
num = []

dfs(0)