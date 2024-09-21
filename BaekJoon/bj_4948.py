import sys
import math

def is_prime(n):
    if(n==1):
        return 0
    
    for i in range(2, int(math.sqrt(n))+1):
        if(n % i == 0):
            return 0
    
    return 1

prime_num = []

for i in range(2, (2*123456)+1):
    if(is_prime(i)):
        prime_num.append(i)

while(1):
    N = int(sys.stdin.readline())
    cnt = 0
        
    if(N == 0):
        break

    for i in prime_num:
        if(N< i <= 2*N):
            cnt += 1
    print(cnt)
