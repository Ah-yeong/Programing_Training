def dp(arr):
    l = len(arr)
    dp = [0] * (l+1)
    dp[0] = 0
    dp[1] = arr[0]
    dp[2] = min(arr[0], arr[1])
    
    if l <= 2:
        return dp[l]
    
    for i in range(3, l+1):
        dp[i] = min(dp[i-1], dp[i-2]) + arr[i-1]
        
    return min(dp[l-1], dp[l])

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    arr2 = [3, 1, 1, 40, 1]
    arr3 = [100, 1, 50, 1, 30, 1]
    
    print(dp(arr1))
    print(dp(arr2))
    print(dp(arr3))


