import sys

n = int(sys.stdin.readline())

start = 0
end = n

while start <= end:
    mid = (start + end) // 2
    if(mid * mid >= n):
        result = mid
        end = mid - 1
    else:
        start = mid +1

print(result)