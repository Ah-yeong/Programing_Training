import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
k = int(sys.stdin.readline())

start = end = 0
sum = cnt = 0

while start < n:
    while sum < k and end < n:
        sum += num[end]
        end += 1
    
    if sum > k:
        cnt += 1
    else:  
        sum -= num[start]
        start += 1

print(cnt)