from collections import defaultdict
import sys

N, M = map(int, sys.stdin.readline().split())

name = defaultdict(int)
result = []

for _ in range(N):
    temp = sys.stdin.readline()
    name[temp] += 1
print(name)

for _ in range(M):
    temp = sys.stdin.readline()
    if temp in name:
        result.append(temp)

result.sort()

print(len(result))

for i in result:
    print(i.strip())