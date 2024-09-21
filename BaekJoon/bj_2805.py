import sys

N, M = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for i in tree:
        if(i > mid):
            sum += i - mid

    if(sum >= M):
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)