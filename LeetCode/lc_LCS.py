class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[-1]*1001 for _ in range(1001)]
        
        return self.LCS(m, n, text1, text2, memo)
    
    def LCS(self, m, n, text1, text2, memo):
        if memo[m][n] != -1:
            return memo[m][n]
        
        if m == 0 or n == 0:
            return 0
        
        elif text1[m-1] == text2[n-1]:
            memo[m][n] = self.LCS(m-1, n-1, text1, text2, memo) + 1
            return memo[m][n]
        
        else:
            memo[m][n] = max(self.LCS(m-1, n, text1, text2, memo), self.LCS(m, n-1, text1, text2, memo))
            return memo[m][n]
