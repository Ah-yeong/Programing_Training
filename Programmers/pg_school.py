def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    dp[1][1] = 1   
    
    for x, y in puddles:
        dp[y][x] = 0
        
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1:
                continue
            elif [j,i] in puddles:
                continue
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    answer = dp[n][m] % 1000000007
    return answer
