import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[0] for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, i + 2):
        if j == 1 or j == i+1:
            dp[i].append(1)
        else:
            dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])

print(dp[N][K+1] % 10007)