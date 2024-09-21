import sys

N = int(sys.stdin.readline())
power = list(map(int, sys.stdin.readline().split()))
power.reverse()

dp = [0] * N

for i in range(N):
    key = 0
    for j in range(i):
        if power[i] > power[j]:
            if key < dp[j]:
                key = dp[j]
    dp[i] = key + 1

print(dp)
print(N-max(dp))