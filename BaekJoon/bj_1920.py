import sys

def binary_search(arr, key):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2
        if key == arr[mid]:
            return 1
        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

n.sort()

for i in range(M):
    print(binary_search(n, m[i]))