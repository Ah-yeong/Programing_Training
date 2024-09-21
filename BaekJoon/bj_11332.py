import sys
import math

C = int(sys.stdin.readline())

for _ in range(C):
    S, N, T, L = map(str, sys.stdin.readline().split())

    n = int(N)
    t = int(T)
    l = int(L)

    if S == "O(N)":
        time = n * t
    elif S == "O(N^2)":
        time = (n**2) * t
    elif S == "O(N^3)":
        time = (n**3) * t
    elif S == "O(2^N)":
        time = (2**n) * t  
    else:
        time = math.factorial(n) * t

    if time <= l * 100000000:
        print("May Pass.")
    else:
        print("TLE!")
