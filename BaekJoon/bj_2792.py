import sys

N, M = map(int,sys.stdin.readline().split())
jewel = []

for _ in range(M):
    jewel.append(int(sys.stdin.readline()))

start = 1
end = max(jewel)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in jewel:
        if(mid <= i):
            if max < ((i // mid) + (i % mid) - 1):
                max = (i // mid) + (i % mid) - 1
            cnt += i // mid
        else:
            if max < i:
                max = i
            cnt += 1
    if cnt >= N:
        result = max
        start = mid + 1
    else:
        end = mid - 1
    print(mid, cnt, max)

print(result)
    