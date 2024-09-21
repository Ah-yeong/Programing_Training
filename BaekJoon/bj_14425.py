import sys

N, M = map(int, sys.stdin.readline().split())

S = set()
cnt = 0

for i in range(N):
    S.add(sys.stdin.readline())

for i in range(M):
    temp = sys.stdin.readline()
    if temp in S:
        cnt += 1

print(cnt)
