import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
loca = list(map(int, sys.stdin.readline().split()))

start = 1
end = N

flag = 0
result = 0

while start <= end:
    mid = (start + end) // 2
    flag = 0

    if loca[0]-mid > 0:
        flag = 1
    for i in range(0,M-1):
        if((loca[i+1]- loca[i]) / 2) > mid:
            flag = 1
            break
    if N - mid >loca[M-1]:
        flag = 1
    
    if flag == 1:
        start = mid + 1
    else:
        end = mid -1
        result = mid

print(result)