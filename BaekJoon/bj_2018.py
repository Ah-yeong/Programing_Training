import sys

N = int(sys.stdin.readline())

cnt = 1
start = cnt
result = 0
sum = 0

while cnt < N:
    if sum < N:
        sum += start
        start += 1
    
    if sum == N or start == N:
        sum = 0
        result += 1
        cnt += 1
        start = cnt
    
print(result)