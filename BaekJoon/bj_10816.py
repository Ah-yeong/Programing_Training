import sys

def binary_search(num, arr, key):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2

        if key == arr[mid]:
            return num[key]
        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0

N = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

num = {}

for i in range(N):
    if n[i] not in num:
        num[n[i]] = 1
    else:
        num[n[i]] += 1

n.sort()

for i in range(M):
    result = binary_search(num, n, m[i])
    print(result, end=" ")
