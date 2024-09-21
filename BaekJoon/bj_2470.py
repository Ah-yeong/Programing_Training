import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num.sort()
start = 0
end = N-1
min = 2000000000

while start < end:
    if abs(num[start] + num[end]) < min:
        min = abs(num[start] + num[end])
        result1 = num[start]
        result2 = num[end]

    if num[start] + num[end] < 0:
        start += 1
    else:
        end -= 1

print(result1, result2)