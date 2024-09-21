import sys

prime = [True for i in range(10001)]
prime[0] = False
prime[1] = False

for i in range(2, int(10001**(1/2))+1):
    if(prime[i] == 0):
        continue
    for j in range(i*2, 10001, i):
        prime[j] = False

prime_num = []

for i in range(10001):
    if(prime[i] == True):
        prime_num.append(i)

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    index = 0
    temp = 0
    
    while (n - prime_num[index]) >= prime_num[index]:
        if prime[n - prime_num[index]] == True:
            if(temp < prime_num[index]):
                temp = prime_num[index]
        index += 1
    print(temp, n-temp)
