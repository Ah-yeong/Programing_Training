import sys

X = int(sys.stdin.readline())

if X== 1:
    print("1/1")

else:
    cnt = 1

    while(X>0):
        X -= cnt
        cnt += 1

    num = cnt-1
    A = B = num

    if num % 2 == 0:
        A += X
        B -= (X + 1)
    else:
        B += X
        for _ in range(num):
            A -= 1
    print(cnt, X)
    print(A,"/", B)