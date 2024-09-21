import sys

T = int(sys.stdin.readline())
num1 = num2 = 1

for i in range(T):
    num1 = num2 = 1
    N, M = map(int, sys.stdin.readline().split())
    for j in range(M, M-N, -1):
        num1 *= j
    for k in range(N, 0, -1):
        num2 *= k
    print(num1//num2)

