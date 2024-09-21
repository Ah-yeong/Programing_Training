import sys

N = int(sys.stdin.readline())

sum = 0
num = 1

while N >= sum:
    sum += num
    num += 1

print(num-2)