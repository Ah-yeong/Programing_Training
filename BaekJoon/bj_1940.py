import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num.sort()
start = 0
end = N-1
cnt = 0

while start < end:
    if num[start] + num[end] == M:
        cnt += 1
        start += 1
        end -= 1
    elif num[start] + num[end] < M:
        start += 1
    else:
        end -=1

print(cnt)