import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    rank = []
    
    for _ in range(N):
        r1, r2 = map(int, sys.stdin.readline().split())
        rank.append([r1,r2])

    rank.sort(key = lambda x:x[0])
    min = rank[0][1]
    cnt = 0

    for i in range(N):
        if min > rank[i][1]:
            min = rank[i][1]
            cnt += 1

    print(cnt+1)



