import sys

string = sys.stdin.readline()
S = []

for i in range(len(string)-1):
    S.append(string[i:])

S.sort()

for i in S:
    print(i, end="")