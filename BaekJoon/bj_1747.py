import sys
import math

def is_prime(n):
    if(n==1):
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if(n % i == 0):
            return False
    
    return True

def is_palindrome(n):
    for i in range(0, len(n)//2):
        if(n[i] == n[len(n)-1-i]):
            continue
        else:
            return False
    return True
        

N = int(sys.stdin.readline())

while True:
    if(is_prime(N)):
        if(is_palindrome(str(N))):
            break
    N += 1

print(N)
    