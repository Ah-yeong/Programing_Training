import sys

X, Y = map(int,sys.stdin.readline().split())
N = int(sys.stdin.readline())

x = [0, X]
y = [0, Y]

for _ in range(N):
    n, m = map(int,sys.stdin.readline().split())
    if n == 1:
        x.append(m)
    else:
        y.append(m)
x.sort()
y.sort()

max_x = 0
max_y = 0

for i in range(len(x)-1):
    if(max_x < x[i+1]-x[i]):
        max_x =  x[i+1]-x[i]

for i in range(len(y)-1):
    if(max_y < y[i+1]-y[i]):
        max_y =  y[i+1]-y[i]

print(max_x * max_y)