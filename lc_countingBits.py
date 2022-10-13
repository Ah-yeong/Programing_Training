class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = [0] * (n+1)
        cnt = 1

        for i in range(1, n+1):
            if i == 2 * cnt:
                cnt *= 2
            memo[i] = memo[i-cnt] + 1
            
        return memo