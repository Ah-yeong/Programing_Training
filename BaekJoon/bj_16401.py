import sys

M, N = map(int, sys.stdin.readline().split())
snack = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(snack)
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in snack:
        cnt += i // mid

    if cnt >= M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)