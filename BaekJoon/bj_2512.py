import sys

N = int(sys.stdin.readline())
money = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

start = 0
end = max(money)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in money:
        if(i >= mid):
            sum += mid
        else:
            sum += i

    if(sum <= M):
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)