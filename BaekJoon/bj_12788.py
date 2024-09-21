import sys

N = int(sys.stdin.readline())
M, K =  map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

A.sort(reverse=True)

pen = M*K
sum = 0
cnt = 0

for i in range(N):
    if(sum < pen):
        sum += A[i]
        cnt += 1
    else:
        break

if sum < pen:
    print("STRESS")
else:
    print(cnt)
