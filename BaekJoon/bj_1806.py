import sys

N, S = map(int,sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))


start = 0
end = 0
sum = 0
len = N+1

while start < N:
    if sum >= S and end <= N:
        print(sum, start, end)
        len = min(len, end-start)
        sum -= num[start]
        start += 1

    else:
        sum += num[end]
        end += 1
    
    if end == N:
        break
    
if len == N+1:
    print(0)
else:
    print(len)