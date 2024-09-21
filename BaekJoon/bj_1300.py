import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 1
end = k
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, mid+1):
        for j in range(1, N+1):
            if(i%j == 0):
                print(i, end = " ")
                cnt += 1

    print("-", cnt)
    if(cnt-1 >= k):
        end = mid - 1 
        result = i
    else:
        start = mid + 1

print(result)



