import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
sum = int(sys.stdin.readline())

num.sort()
start = 0
end = n-1
cnt = 0

while start < end:
    if num[start] + num[end] == sum:
        cnt += 1
        start += 1
        end -= 1
    elif num[start] + num[end] < sum:
        start += 1
    else:
        end -=1

print(cnt)

