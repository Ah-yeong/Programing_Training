import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
mine = list(map(int, sys.stdin.readline().split()))

card.sort()

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

for i in range(M):
    print(binary_search(card, mine[i]), end=" ")
