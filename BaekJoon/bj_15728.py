import sys

N, K =  map(int, sys.stdin.readline().split())
s_card = list(map(int, sys.stdin.readline().split()))
t_card = list(map(int, sys.stdin.readline().split()))

for _ in range(K):
    max = -1000000001
    for i in range(N):
        for j in range(N):
            if (s_card[i] * t_card[j] > max and t_card[j] != 10001):
                max = s_card[i] * t_card[j]
                idx = j
    t_card[idx] = 10001

max = -100000001
for i in range(N):
    for j in range(N):
        if(s_card[i] * t_card[j] > max):
            if(t_card[j] < 10001):
                max = s_card[i] * t_card[j]
print(max)