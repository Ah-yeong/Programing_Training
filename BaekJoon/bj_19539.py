import sys

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))

cnt1 = cnt2 = 0

for i in range(N):
    cnt1 += num[i] // 2
    cnt2 += num[i] % 2

if(sum(num) % 3 == 0):
    if(cnt1 >= cnt2):
        print("YES")
    else:
        print("NO")

else:
    print("NO")
