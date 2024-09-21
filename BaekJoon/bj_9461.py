import sys

p = [1,1,1,2,2]

T = int(sys.stdin.readline())
cnt = 0

for i in range(T):
    N = int(sys.stdin.readline())
    if N <= len(p):
        print(p[N-1])
    else:
        for j in range(len(p), N):
            p.append(p[j-1] + p[cnt])
            cnt += 1
        print(p[N-1])
