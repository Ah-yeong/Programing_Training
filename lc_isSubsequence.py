class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)
        
        if s == '':
            return True
        
        elif t =='':
            return False
        
        else:
            if(s[sLen-1] == t[tLen-1]):
                s = s[:-1]
                t = t[:-1]
                return self.isSubsequence(s, t)
            else:
                t = t[:-1]
                return self.isSubsequence(s, t);