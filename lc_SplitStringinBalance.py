class Solution(object):
    def balancedStringSplit(self, s):
        Lcnt = 0
        Rcnt = 0
        result = 0
        
        for i in range(len(s)):
            if s[i] == 'R':
                Rcnt += 1
            elif s[i] == 'L':
                Lcnt += 1
            
            if Rcnt == Lcnt:
                result += 1
                Rcnt = Lcnt = 0
        
        return result