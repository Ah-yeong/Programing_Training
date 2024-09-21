import sys

K, N = map(int, sys.stdin.readline().split())
line = []

for _ in range(K):
    line.append(int(sys.stdin.readline()))

start = 0
end = max(line)

while start <= end:
    mid = (start + end) // 2
    if(mid == 0):
        break
    sum = 0
    for i in line:
        if(i >= mid):
            sum += i // mid

    if(sum >= N):
        start = mid + 1
        result = mid
    else:
        end = mid - 1

if(mid == 0):
    print(1)
else:
    print(result)