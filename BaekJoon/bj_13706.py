import sys

N = int(sys.stdin.readline())

start = 0
end = N

while start <= end:
    mid = (start + end) // 2
    temp = mid*mid
    if temp == N: 
        break
    elif temp < N:
        start = mid + 1
    else:
        end = mid - 1

print(mid)