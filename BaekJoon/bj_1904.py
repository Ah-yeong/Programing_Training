import sys

N = int(sys.stdin.readline())

n = []

n.append(0)
n.append(1)
n.append(2)
cnt = 2

while(cnt != N):
    n.append(n[cnt-1]+n[cnt])
    cnt += 1

print(n[-1])
