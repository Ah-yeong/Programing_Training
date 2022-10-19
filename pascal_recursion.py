import sys

def pascal_recursion(n,m):
    if m == 1 or n == 1 or m == n:
        return 1
    else:
        return pascal_recursion(n-1, m-1) + pascal_recursion(n-1, m)
'''  
디피로 왜 안풀리냐
def pascal_dp(n,m):
    dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
    
    for i in range(1, n+1):
        dp[i][1] = 1
        dp[i][i] = 1
        
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    print(dp)
    return dp[n][m]
'''

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    print(pascal_recursion(n,m))
    #print(pascal_dp(5,3))