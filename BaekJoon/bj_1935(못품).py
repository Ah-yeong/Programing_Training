import sys

N = int(sys.stdin.readline())
stack = []
num = []

postfix = list(sys.stdin.readline())

for i in range(N):
    num.append(sys.stdin.readline())

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(postfix)):
    if postfix[i].isalpha == True:
        postfix[i] = num[alpha.index(postfix[i])]

print(postfix)
