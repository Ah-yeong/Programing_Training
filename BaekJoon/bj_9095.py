import sys

def num(n):
    if n == 1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return num(n-1)+num(n-2)+num(n-3)

T= int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    print(num(n))