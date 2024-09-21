import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num.sort()
sum1= 0
sum2=0

if N % 2 ==0:
    for i in range(N):
        sum1 += abs(num[i] - num[N//2])
        sum2 += abs(num[i] - num[N//2-1])
    if sum1>=sum2:
        print(num[N//2-1])
    else:
        print(num[N//2])

else:
    print(num[N//2])
