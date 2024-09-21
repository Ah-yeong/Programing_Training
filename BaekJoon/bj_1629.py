import sys

def pow(a, b, c):
    if(b == 1):
        return a % c

    temp = pow(a, b//2, c)

    if(b % 2 == 0):
        return temp * temp % c
    else:
        return temp * temp * a % c

A,B,C = map(int, sys.stdin.readline().split())
print(pow(A,B,C))
