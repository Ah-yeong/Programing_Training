import sys

A, B = map(int, sys.stdin.readline().split())

cnt = flag = 0

while A != B:
    cnt += 1
    B_list = list(map(int, str(B)))

    if B < A:
        flag = 1
        break

    if B_list[len(B_list)-1] == 1:
        del B_list[len(B_list)-1]
        B = (B-1) // 10

    elif B % 2 == 0:
        B = B // 2

    else:
        flag = 1
        break

if flag == 1:
   print(-1) 

else:
    print(cnt+1)