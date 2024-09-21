import sys

def dfs(cnt):
    if(cnt == 6):
        for i in num:
            print(i, end = " ")
        print()
        return
    
    for i in range(0, len(S)):
        if(check[i]):
            continue
    
        check[i] = True
        num.append(S[i])
        dfs(cnt + 1)
        num.pop()
        for j in range(i+1, len(S)):
            check[j] = False

while True: 
    S = list(map(int, sys.stdin.readline().split()))
    
    if(S[0] == 0):
        break

    del S[0]

    check = [False] * (len(S))
    num = []

    dfs(0)
    print()