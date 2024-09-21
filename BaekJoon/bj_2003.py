import sys

N, M = map(int,sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

start = end = 0
sum = cnt = 0

while start < N:
    while sum < M and end < N:
        sum += num[end]
        end += 1
    
    if sum == M:
        cnt += 1
        
    sum -= num[start]
    start += 1

print(cnt)

    
