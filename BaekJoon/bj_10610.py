import sys

n = int(sys.stdin.readline())
num = list(map(int, str(n)))

max = 0

for i in range(len(num)):
    for j in range(len(num)):
        if i != j:
            
