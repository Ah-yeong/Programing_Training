import sys

def binary_search(b, key, m):
    start = 0
    end = m-1
    result = -1

    while start <= end:
        mid = (start + end) // 2
        if key > b[mid]:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    B.sort()
    cnt = N

    for i in A:
        cnt += binary_search(B, i, M)
    print(cnt)