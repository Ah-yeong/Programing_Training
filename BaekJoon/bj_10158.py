import sys

w,h = map(int, sys.stdin.readline().split())
p,q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

x = (p+t) % (2*w)
y = (q+t) % (2*h)

if x > w:
    x = 2*w - x

if y > h:
    y = 2*h - y

print(x, y)