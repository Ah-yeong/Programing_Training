import sys

N, C = map(int, sys.stdin.readline().split())
X = []

for _ in range(N):
    X.append(int(sys.stdin.readline()))

X.sort()

start = 1
end = X[-1] - X[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    temp = X[0]
    cnt = 1

    for i in range(1, N):
        if temp + mid <= X[i]:
            cnt += 1
            temp = X[i]

    if cnt >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)