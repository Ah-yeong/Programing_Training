n = 5
m = 3

dp = [[0]*(n) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j == 0:
            dp[i][j] = 1
        elif i == j:
            dp[j][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n-1][m-1])