import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [0] * N

for i in range(N):
    key = 0
    for j in range(i):
        if A[i] > A[j]:
            if key < dp[j]:
                key = dp[j]
    dp[i] = key + 1

print(max(dp))
