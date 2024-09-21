import sys

n, T = map(int, sys.stdin.readline().split())
time = list(map(int, sys.stdin.readline().split()))

sum = 0
cnt = 0

for i in range(n):
    if(sum + time[i] > T):
        break
    sum += time[i]
    cnt += 1

print(cnt)


