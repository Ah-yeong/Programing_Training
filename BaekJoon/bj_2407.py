import sys

num1 = num2 = 1

N, M = map(int, sys.stdin.readline().split())
for j in range(N, N-M, -1):
    num1 *= j
for k in range(M, 0, -1):
    num2 *= k
print(int(num1//num2))