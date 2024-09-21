import sys

N, M = map(int,sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

sum = A+B
sum.sort()

for i in sum:
    print(i, end=" ")