import sys

M, N = map(int, sys.stdin.readline().split())
num = [i for i in range(N+1)]

num[1] = 0

for i in range(2, int(N**(1/2))+1):
    if(num[i]== 0):
        continue
    for j in range(i*2, N+1, i):
        num[j] = 0

for i in range(M, N+1):
    if(num[i] != 0):
        print(num[i])