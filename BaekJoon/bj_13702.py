import sys

N, K = map(int, sys.stdin.readline().split())
drink = []

for _ in range(N):
    drink.append(int(sys.stdin.readline()))

start = 1
end = max(drink)
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in drink:
        cnt += i // mid

    if cnt >= K:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)