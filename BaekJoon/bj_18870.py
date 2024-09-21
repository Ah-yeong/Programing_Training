import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num_sort = list(sorted(set(num)))

num_sort = {num_sort[i]:i for i in range(len(num_sort))}

print(*[num_sort[i] for i in num])