import sys

T = int(sys.stdin.readline())
sum = []

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    num = [[i for i in range(1,n+1)] for _ in range(k+1)]
    
    for i in range(1, k+1):
        sum = 0
        for j in range(n):
            sum += num[i-1][j]
            num[i][j] = sum
            
    print(num[k][n-1])
    
