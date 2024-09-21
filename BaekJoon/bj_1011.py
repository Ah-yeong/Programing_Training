import sys

T = int(sys.stdin.readline())
distance = [1,2]

for _ in range(T):
    start, end = map(int, sys.stdin.readline().split())
    num = 2
    flag = 1
    while(distance[-1] < end - start):
        distance.append(distance[-1] + num)
        if(flag == 1):
            flag = 0
        else:
            num += 1
    if(end - start == 1):
        print(1)
    else:
        print(len(distance))
