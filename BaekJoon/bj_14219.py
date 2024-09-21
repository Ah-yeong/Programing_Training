import sys

N,M = map(int, sys.stdin.readline().split())

if (N*M)%3 == 0:
    print("YES")
else:
    print("NO")