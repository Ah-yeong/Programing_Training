import sys

T = int(sys.stdin.readline())

fibo = [1,2]

for i in range(2,43):
    fibo.append(fibo[i-2]+fibo[i-1])

for _ in range(T):
    n = int(sys.stdin.readline())
    result = []
    while n != 0:
        for i in range(42, -1,-1):
            if n >= fibo[i]:
                temp = fibo[i]
                break
        n -= temp
        result.append(temp)
    result.sort()
    for i in result:
        print(i, end=" ")
