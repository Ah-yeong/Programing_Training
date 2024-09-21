class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {}
        return self.memoization(n, memo)
        
    def memoization(self, n, memo):
        if n in memo:
            return memo[n]
        
        if n == 1:
            memo[n] = 0 
            return memo[n]
        
        if n % 2 == 0:
            memo[n] =  1 + self.memoization(n/2, memo)
        else:
            memo[n] =  1 + min(self.memoization(n-1, memo), self.memoization(n+1, memo))
        
        return memo[n]
