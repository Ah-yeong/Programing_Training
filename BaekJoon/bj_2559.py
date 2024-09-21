import sys

N, M = map(int,sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

S = 0
sum = [0]

for i in range(N):
    S += num[i]
    sum.append(S)

result = []

for i in range(N-M+1):
    result.append(sum[i+M] - sum [i])

print(max(result))