import sys

N = int(sys.stdin.readline())
weight = []

for i in range(N):
    w = int(sys.stdin.readline())
    weight.append(w)

weight.sort(reverse=True)

for i in range(N):
    weight[i] *= i+1

print(max(weight))
