from collections import deque

def get_answer(N, num):
    d = deque()
    num.sort(reverse= True)

    for i in range(N):
        if i % 2== 0:
            d.appendleft(num[i])
        else:
            d.append(num[i])

    max = -1

    for i in range(N-1):
        temp = abs(d[i] - d[i + 1])
        if max < temp:
            max = temp

    temp = abs(d[0] - d[N - 1])

    if max < temp:
        max = temp

    print(max)

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    get_answer(N, arr)
