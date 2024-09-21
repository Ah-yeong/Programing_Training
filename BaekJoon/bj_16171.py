import sys

S = sys.stdin.readline()
K = sys.stdin.readline()
num = [0,1,2,3,4,5,6,7,8,9]
string = []

for i in range(len(S)):
    if ord(S[i]) >= 48 and ord(S[i]) <= 57:
        continue  
    else:
        string.append(S[i])

string = ''.join(string)
if K in string:
    print(1)
else:
    print(0)