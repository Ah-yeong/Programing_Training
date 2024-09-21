import sys
n = int(sys.stdin.readline())
num = [[int(x) for x in sys.stdin.readline().split()] for y in range(n)]

for i in range(n-1):
    for j in range(i+2):
        if(j==0):
            num[i+1][j] += num[i][j]
        elif(j==i+1):
            num[i+1][j] += num[i][j-1]
        else:
            num[i+1][j] += max(num[i][j-1], num[i][j])

print(max(num[n-1]))