class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        memo = [[None]*31 for i in range(31)]
        result = []
        
        _ = self.generate_memo(numRows, numRows,memo)
        
        for i in range(numRows):
            result.append(memo[i][:i+1])
            result[i][i] = 1
        
        return result
    
    def generate_memo(self, m, n, memo):
        if memo[m][n] != None:
            return memo[m][n]
        
        if m == n:
            memo[m][n] = 1
            
        if n == 0:
            memo[m][n] = 1
            return memo[m][n]
        
        else:
            memo[m][n] = self.generate_memo(m-1, n-1, memo) + self.generate_memo(m-1, n,memo)
            return memo[m][n]