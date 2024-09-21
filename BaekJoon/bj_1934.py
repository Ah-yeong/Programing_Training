import sys

def gcd(a,b):
    if a < b:
        a,b = b,a
    if b == 0:
        return a
    elif a % b == 0:
        return b
    else:
        return gcd(b, a%b)

T = int(sys.stdin.readline())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A*B//gcd(A,B))