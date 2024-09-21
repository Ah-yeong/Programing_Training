import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    value = deque()
    index = deque()
    N, M = map(int, sys.stdin.readline().split())
    num = list(map(int, sys.stdin.readline().split()))

    for i in range(N):
        value.append(num[i])
        index.append(i)
    
    num.sort()

    cnt = 0

    while(True):
        if(value[0] < num[-1]):
            temp = value.popleft()
            value.append(temp)
            temp = index.popleft()
            index.append(temp)
        else:
            value.popleft()
            num.pop()
            cnt += 1 
            if(index[0] == M):
                break
            else:
                index.popleft()

    print(cnt)




