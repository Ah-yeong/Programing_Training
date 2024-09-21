import sys

def num_count(N,K):
    cnt = 0
    for i in range(2, N+2):
        if(num[i] == False):
            continue
        for j in range(i, N+1, i):
            if(num[j] == True):
                num[j] = False
                cnt += 1
                if(cnt == K):
                    return j

N, K = map(int, sys.stdin.readline().split())

num = [True for _ in range(N+2)]
num[0] = False
num[1] = False

print(num_count(N,K))