import sys

N, M = map(int, sys.stdin.readline().split())

floor = []

for _ in range(N):
    floor.append(list(sys.stdin.readline()))

temp = []
for _ in range(M):
    temp.append('\n')

floor.append(temp)

cnt = 0

for i in range(N):
    for j in range(M+1):
        if floor[i][j] == '-':
            if floor[i][j] != floor[i][j+1]:
                cnt += 1

for i in range(N+1):
    for j in range(M):
        if floor[i][j] == '|':
            if floor[i][j] != floor[i+1][j]:
                cnt += 1

print(cnt)
