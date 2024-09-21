import sys

num = [[1,1,1,0,1,1,1], [0,0,1,0,0,1,0], [1,0,1,1,1,0,1], [1,0,1,1,0,1,1], [0,1,1,1,0,1,0], [1,1,0,1,0,1,1], [1,1,0,1,1,1,1], [1,0,1,0,0,1,0], [1,1,1,1,1,1,1], [1,1,1,1,0,1,1]]

N, K, P, X = map(int, sys.stdin.readline())

x = ''.join(str[X])
idx = 0
cnt = 0

for i in range(K):
    for j in range(10):
        cnt = 0
        if j != x[i]:
            for idx in range(10):
                if num[j][idx] != num[x[i]][idx]:
                    cnt += 1
        print()

