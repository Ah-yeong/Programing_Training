import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    if(N == 0):
        print("1","0")
    elif(N == 1):
        print("0","1") 
    else:  
        fibo = [0 for i in range (N+1)]
        fibo[1] = 1
        for i in range(2,N+1):
            fibo[i] = fibo[i-1] + fibo[i-2]
        print(fibo[N-1], fibo[N])