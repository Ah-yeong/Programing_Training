import sys

num = [i for i in range(1299710)]
num[0] = 0
num[1] = 0

for i in range(2, int(1299710**(1/2))+1):
    if(num[i] == 0):
        continue
    for j in range(i*2, 1299710, i):
        num[j] = 0

T = int(sys.stdin.readline())


for _ in range(T):
    k = int(sys.stdin.readline())
    start = 0
    end = k*k

    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        check = []
        for i in range(mid):
            if(num[i] != 0):
                cnt += 1
                check.append(i)
        if(cnt > 2):
            

