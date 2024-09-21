import sys

L, R = map(int, sys.stdin.readline().split(' '))
cnt = 0

if len(str(L)) == len(str(R)):
    l = str(L)
    r = str(R)
    for i in range(len(l)):
        if l[i] == r[i]:
            if(l[i] == '8'):
                cnt +=1
        else:
            break

print(cnt)